from cpxmath import analyze, visualize, parse_function, analyze_domain
from cpxmath.support import UnsupportedFunctionError

f = input("Enter a function of z: ")

try:
    parsed_expr = parse_function(f)
except ValueError as e:
    print(f"error parsing given function: {e}")
    raise SystemExit

result = analyze(parsed_expr.eval_expr)

for name, block in result.items():
    if isinstance(block, dict):
        print(name)
        for key, value in block.items():
            print(f"  {key}: {value}")
    else:
        print(f"{name}: {block}")

print("\nDomain Analysis:")
try:
    domain_result = analyze_domain(parsed_expr)
    for output in domain_result.values():
        print(output)
except UnsupportedFunctionError as e:
    print(f"domain: {e}")

visualize(parsed_expr.eval_expr)