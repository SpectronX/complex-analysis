import sympy as sp

from .symbols import z

allowed_functions = (sp.exp, sp.sin, sp.cos)
error_msg = "Not supported. Supported: polynomials, rational, exponential, trigonometric."

# for method 2
# allowed_functions = (sp.sin, sp.cos, sp.exp, sp.tan, sp.cot, sp.sec, sp.csc)
# denoms = {sp.tan: sp.cos, sp.sec: sp.cos, sp.cot: sp.sin, sp.csc: sp.sin}

def check_supported(expr):
    for f in expr.atoms(sp.Function):
        if not isinstance(f, allowed_functions) or not f.args[0].is_polynomial(z):
            raise ValueError(error_msg)
    for p in expr.atoms(sp.Pow):
        if p.base.has(z) and (p.exp.has(z) or not p.exp.is_Integer):
            raise ValueError(error_msg)

def denoms(expr):
    d = []
    for node in sp.preorder_traversal(expr):
        if node.is_Pow and node.exp.could_extract_minus_sign():
            d.append(node.base)

        # for method 2
        # elif node.func in denoms:
        #   d.append(denoms[node.func](node.args[0]))

    return d

