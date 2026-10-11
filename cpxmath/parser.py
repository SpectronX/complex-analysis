import sympy as sp

from .symbols import z
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from dataclasses import dataclass

transformations = (standard_transformations + (implicit_multiplication_application))

expr_map = {
    "pi": sp.pi,
    "e": sp.E,
    "i": sp.I,
    "log": sp.log,
    "conjugate": sp.conjugate,
}

@dataclass
class ParsedFunction:
    user_input: str
    raw_expr: sp.Expr
    eval_expr: sp.Expr

def parse_function(function):
    try: 
        norm_str = function.replace("^", "**")
        raw_expr = parse_expr(norm_str, local_dict={expr_map}, transformations=transformations, evaluate=False)
        eval_expr = parse_expr(norm_str, local_dict={expr_map}, transformations=transformations, evaluate=True)
        if eval_expr.free_symbols - {z}:
            raise ValueError(f"Function might contain invalid symbols: {eval_expr.free_symbols - {z}}")
        return ParsedFunction(function, raw_expr, eval_expr)
    except (SyntaxError, TypeError, ValueError) as error:
        raise ValueError(f"Invalid function: {function}. {type(error).__name__}: {error}") from error