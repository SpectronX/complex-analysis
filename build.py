import json, html
from pathlib import Path
from markdown_it import MarkdownIt

# pygments imports for syntax highlighting of code blocks.
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter

# configuration of paths for directories and files.
# -------------------------------------------------
MAIN_DIR = Path(__file__).resolve().parent

NOTES_DIR = MAIN_DIR / "notes"
FIGURES_DIR = MAIN_DIR / "figures"
DOCS_DIR = MAIN_DIR / "docs"

PICS_MAIN_DIR = FIGURES_DIR
PICS_DOCS_DIR = DOCS_DIR / "figures"

CSS_MAIN_FILE = MAIN_DIR / "style.css"
CSS_DOCS_FILE = DOCS_DIR / "style.css"

# the css file is a required asset for the build process.
if not CSS_MAIN_FILE.exists():
    raise FileNotFoundError(
        f"CSS file '{CSS_MAIN_FILE}' not found."
    )

# they contain the files that will be processed and generated during the build process.
Path.mkdir(DOCS_DIR, exist_ok=True)
Path.mkdir(FIGURES_DIR, exist_ok=True)
Path.mkdir(PICS_DOCS_DIR, exist_ok=True)

md_files = list(NOTES_DIR.glob("*.md")) # list of markdown files
figure_files = list(PICS_MAIN_DIR.glob("*.png")) # list of figure files
code_files = list(PICS_MAIN_DIR.glob("*.ipynb")) # list of code files

expected_html_files = [(DOCS_DIR / md_file.name).with_suffix(".html") for md_file in md_files]
actual_html_files = list(DOCS_DIR.glob("*.html"))

expected_figure_files = [(PICS_DOCS_DIR / pic.name) for pic in figure_files]
actual_figure_files = list(PICS_DOCS_DIR.glob("*.png"))

expected_code_files = [(PICS_DOCS_DIR / code.name) for code in code_files]
actual_code_files = list(PICS_DOCS_DIR.glob("*.ipynb"))

# checks for stale files
def remove_stale_files(actual_files, expected_files):
    for file in actual_files:
        if file not in expected_files:
            file.unlink()

remove_stale_files(actual_html_files, expected_html_files)
remove_stale_files(actual_figure_files, expected_figure_files)
remove_stale_files(actual_code_files, expected_code_files)


# copy of static assets from /figures and style.css to /docs/figures and /docs/style.css
CSS_DOCS_FILE.write_bytes(CSS_MAIN_FILE.read_bytes())

for pic in PICS_MAIN_DIR.glob("*"):
    dest = PICS_DOCS_DIR / pic.name
    dest.write_bytes(pic.read_bytes())


md = MarkdownIt("commonmark", {"html": True}) # initializing the MarkdownIt parser.

# metadata extraction from markdown files
def page_title(text):
    for line in text.splitlines():
        if line.startswith("<!-- title:"):
            return line.split(":", 1)[1].strip().removesuffix("-->").strip()
    return "Untitled"

def get_pages():
    pages = []
    for md_file in md_files:
        html_file = (DOCS_DIR / md_file.name).with_suffix(".html")
        with open(md_file, "r") as f:
            md_content = f.read()
            pages.append({
                "md_file": md_file,
                "html_file": html_file,
                "title": page_title(md_content)
            })
    return pages

page_elements = get_pages()

# navigation details for the HTML pages
def nav(page_elements, check_html_file):
    nav_items = []

    for item in page_elements:
        if item["html_file"].name == check_html_file:
            nav_items.append(f'<li><a href="{item["html_file"].name}" class="active">{item["title"]}</a></li>')
        else:
            nav_items.append(f'<li><a href="{item["html_file"].name}">{item["title"]}</a></li>')
    nav_html = "\n".join(nav_items)
    return f'<nav><ul>{nav_html}</ul></nav>'

# page template for the HTML pages
def page_builder(title, nav, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="style.css">

    <script>
    MathJax = {{
        tex: {{
            inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
        }}
    }};
    </script>

    <script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>

    <title>{title}</title>
</head>

<body>

    <nav>
        <div class="nav-container">
            {nav}
        </div>
    </nav>

    <main>
        <article>
            {body}
        </article>
    </main>

</body>
</html>"""

# find figures and code placeholders in the markdown content
def find_pic(md_content):
    page_pics = []
    for line in md_content.splitlines():
        if line.startswith("<!-- figure:"):
            pic_name = line.split(":")[1].strip().split()[0]

            image = PICS_MAIN_DIR / f"{pic_name}.png"
            code = PICS_MAIN_DIR / f"{pic_name}.ipynb"

            if not image.exists() or not code.exists():
                raise ValueError(
                    f"Either the image or notebook file for "
                    f"'{pic_name}' not found in figures directory."
                )
            page_pics.append(pic_name)
    return page_pics

def get_notebook_code(code):
    notebook = json.loads(code)
    code_cells = [cell for cell in notebook["cells"]
        if cell["cell_type"] == "code"]
    code_info = []
    for cell in code_cells:
        cell_code = "".join(cell["source"])
        code_info.append(cell_code)
    return "\n\n".join(code_info)

# inserts the figures and code into the markdown content.
def insert_pic(md_content):
    find_pics = find_pic(md_content)
    figures = {}
    for index, pic in enumerate(find_pics):
        placeholder = f"FIGURE_PLACEHOLDER_{index}"
        image = f'<img src="figures/{pic}.png" alt="{pic}">'

        code_file = PICS_MAIN_DIR / f"{pic}.ipynb"
        code = get_notebook_code(code_file.read_text())
        code = f"<pre><code>{html.escape(code)}</code></pre>"
        # code = highlight(
        #     code,
        #     PythonLexer(),
        #     HtmlFormatter()
        # )

        figure = f"""
        <div class="figure-container">
            {image}
            {code}
        </div>"""

        figures[placeholder] = figure

        md_content = md_content.replace(f"<!-- figure: {pic} -->", placeholder)
        md_content = md_content.replace(f"<!-- code: {pic} -->", "")
    return md_content, figures

def replace_figures(content, figures):
    for placeholder, figure in figures.items():
        content = content.replace(placeholder, figure)
    return content

# build to generate the HTML files from the md files
def build():
    for page in page_elements:
        with open(page["md_file"], "r") as f:
            md_content = f.read()
            
        md_content, figures = insert_pic(md_content)
        content = md.render(md_content)
        content = replace_figures(content, figures)

        with open(page["html_file"], "w") as f:
            f.write(page_builder(page["title"], nav(page_elements, page["html_file"].name), content))

if __name__ == "__main__":
    build()