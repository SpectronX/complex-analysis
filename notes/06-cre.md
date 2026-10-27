<!-- title: Cauchy-Riemann Equations -->
<!-- order: 6 -->

### Cauchy-Riemann Equations

The Cauchy-Riemann equations are a set of two partial differential equations that provide a necessary condition for a complex function to be differentiable at a point $z_0 = x_0 + iy_0$, that is, for $f'(z_0)$ to exist.

*Theorem:* Suppose that $f(z) = u(x, y) + iv(x, y)$ is defined in a neighborhood of $z_0 = x_0 + iy_0$. If $f$ is differentiable at $z_0$, then the partial derivatives $\frac{\partial u}{\partial x}$, $\frac{\partial u}{\partial y}$, $\frac{\partial v}{\partial x}$, and $\frac{\partial v}{\partial y}$ exist at $(x_0, y_0)$ and satisfy the Cauchy-Riemann equations there:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.$$
Conversely, if the partial derivatives exist and are continuous in a neighborhood of $(x_0, y_0)$ and the Cauchy-Riemann equations hold at $(x_0, y_0)$, then $f$ is differentiable at $z_0$. In either case, $f'(z_0) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}$.

Example: Consider the function $f(z) = z^2 = (x + iy)^2 = x^2 - y^2 + 2ixy$. Here, $u(x, y) = x^2 - y^2$ and $v(x, y) = 2xy$. The partial derivatives are:
$$\frac{\partial u}{\partial x} = 2x, \quad \frac{\partial u}{\partial y} = -2y, \quad \frac{\partial v}{\partial x} = 2y, \quad \frac{\partial v}{\partial y} = 2x.$$
The Cauchy-Riemann equations are satisfied:
$$\frac{\partial u}{\partial x} = 2x = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -2y = -\frac{\partial v}{\partial x}.$$
The partial derivatives are continuous everywhere, so $f(z)$ is differentiable at all points in the complex plane, with $f'(z) = 2x + i2y = 2z$.

### Sufficient Condition for Differentiability

The Cauchy-Riemann equations on their own are only a necessary condition for differentiability. There are functions that satisfy them at a point but are not differentiable there. What makes the condition sufficient is that the partial derivatives must also be continuous in a neighborhood of $z_0$.

What this means is that if the Cauchy-Riemann equations are satisfied at $z_0$ and the partial derivatives are continuous in a neighborhood of $z_0$, then $f(z)$ is differentiable at $z_0$.

Example: Consider the function $f(z) = \sqrt{|xy|}$. Here, $u(x, y) = \sqrt{|xy|}$ and $v(x, y) = 0$. Since $u(x, 0) = 0$ and $u(0, y) = 0$, all four partial derivatives are $0$ at the origin, so the Cauchy-Riemann equations are satisfied there. However, $f$ is not differentiable at $z = 0$. Along the real axis, the difference quotient is $\frac{f(h) - f(0)}{h} = 0$. Along the line $y = x$, with $z = h(1 + i)$ and $h > 0$, it is $\frac{|h|}{h(1 + i)} = \frac{1}{1 + i} \neq 0$. The two directions give different values, so the limit does not exist. The partial derivatives are not continuous near the origin, which is why the theorem does not apply.

Example: Consider the function $f(z) = |z|^2 = x^2 + y^2$. Here, $u(x, y) = x^2 + y^2$ and $v(x, y) = 0$. The partial derivatives are:
$$\frac{\partial u}{\partial x} = 2x, \quad \frac{\partial u}{\partial y} = 2y, \quad \frac{\partial v}{\partial x} = 0, \quad \frac{\partial v}{\partial y} = 0.$$
The Cauchy-Riemann equations require $2x = 0$ and $2y = 0$, so they hold only at the origin. The partial derivatives are continuous everywhere, so $f(z)$ is differentiable at $z = 0$, with $f'(0) = 0$, and nowhere else.