import sympy as sp

from .symbols import z

def analyze(function):

    x, y = sp.symbols("x y", real=True)
    cexpr = x + sp.I * y

    f_cexpr = sp.expand_complex(function.subs(z, cexpr))

    def get_re_im(expr):
        u = sp.re(expr)
        v = sp.im(expr)
        return u, v

    def get_deriv(u, v):
        u_x = sp.simplify(sp.diff(u, x))
        u_y = sp.simplify(sp.diff(u, y))

        v_x = sp.simplify(sp.diff(v, x))
        v_y = sp.simplify(sp.diff(v, y))

        return u_x, u_y, v_x, v_y

    def CR_check(u_x, u_y, v_x, v_y):
        eq1 = sp.simplify(u_x - v_y)
        eq2 = sp.simplify(u_y + v_x)
        eq1_satisfied = eq1 == 0
        eq2_satisfied = eq2 == 0

        return{
            "Cauchy-Riemann Check": {},
            "equation_1": {"u_x": u_x, "v_y": v_y, "satisfied": eq1_satisfied},
            "equation_2": {"u_y": u_y, "-v_x": -v_x, "satisfied": eq2_satisfied},
            "satisfied": eq1_satisfied and eq2_satisfied
        }

    u, v = get_re_im(f_cexpr)
    u_x, u_y, v_x, v_y = get_deriv(u, v)
    return CR_check(u_x, u_y, v_x, v_y)    