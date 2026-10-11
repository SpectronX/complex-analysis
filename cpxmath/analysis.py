import sympy as sp

from .symbols import z

def analyze(function):

    x, y = sp.symbols("x y", real=True)
    cexpr = x + sp.I * y

    f_cexpr = function.subs(z, cexpr)
    f_cexpr = f_cexpr.expand()

    def get_re_im(expr):
        u = sp.re(expr)
        v = sp.im(expr)
        return u, v

    def get_deriv(u, v):
        u_x = sp.diff(u, x)
        u_y = sp.diff(u, y)

        v_x = sp.diff(v, x)
        v_y = sp.diff(v, y)

        return u_x, u_y, v_x, v_y

    def CR_check(u_x, u_y, v_x, v_y):
        eq1 = sp.simplify(u_x - v_y)
        eq2 = sp.simplify(u_y + v_x)
        eq1_satisfied = eq1 == 0
        eq2_satisfied = eq2 == 0

        return{
            "equation_1": {
                "u_x": f"{u_x} \n",
                "v_y": f"{v_y} \n",
                "satisfied": f"{eq1_satisfied} \n"
            },
             "equation_1": {
                "u_y": f"{u_y} \n",
                "v_x": f"{-v_x} \n",
                "satisfied": f"{eq2_satisfied} \n"
            },
            "satisfied": f"{eq1_satisfied and eq2_satisfied} \n"
        }

    u, v = get_re_im(f_cexpr)
    u_x, u_y, v_x, v_y = get_deriv(u, v)
    return analyze(u_x, u_y, v_x, v_y)    