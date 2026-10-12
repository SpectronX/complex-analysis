import sympy as sp

from .symbols import z
from .parser import ParsedFunction
from .support import check_supported, denoms

def analyze_domain(parsed_function: ParsedFunction):
    expression = parsed_function.raw_expr
    check_supported(expression)

    excluded = sp.EmptySet
    for d in denoms(expression):
        excluded |= sp.solveset(d, z, sp.Complexes)

    return {
        "excluded_points": excluded,
        "analytic_everywhere": excluded == sp.EmptySet,
        "analytic_domain": sp.Complexes - excluded
    }