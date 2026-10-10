import sympy as sp

from .symbol import z

def analyze(function):

    x, y = sp.symbols("x y", real=True)
    cpx_var = x + sp.I * y

    f_cpx_var = function.subs(z, cpx_var)
    f_cpx_var_expanded = f_cpx_var.expand()

    def get_re_im(expression):
        u = sp.re(expression)
        v = sp.im(expression)

        return u, v