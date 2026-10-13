import sympy as sp

from .symbols import z
from .parser import ParsedFunction
from .support import check_supported, denoms

from textwrap import indent

def output_format(label, value):
    text = sp.pretty(value)
    if "\n" in text:
        return f"{label}:\n{indent(text, '      ')}"
    return f"{label}: {text}"

def analyze_domain(parsed_function: ParsedFunction):
    expression = parsed_function.raw_expr
    check_supported(expression)

    excluded = sp.EmptySet
    for d in denoms(expression):
        excluded |= sp.solveset(d, z, sp.Complexes)

    if excluded == sp.EmptySet:
        where_analytic = "analytic on: the whole complex plane"
    else:
        where_analytic = "analytic on: the complex plane minus the points above"

    return {
        "excluded_points:": output_format("excluded_points", excluded),
        "analytic_everywhere: ": output_format("analytic_everywhere", excluded == sp.EmptySet),
        "where_analytic:": output_format("where_analytic", where_analytic),
        "analytic_domain:": output_format("analytic_domain", sp.Complexes - excluded)
    }