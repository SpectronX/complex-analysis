<!-- title: Continuity & Derivatives -->
<!-- order: 5 -->

### Continuity

A function $f(z)$ is said to be continuous at a point $z_0$ in its domain if the following three conditions are satisfied:
1. $f(z_0)$ is defined.
2. $\lim_{z \to z_0} f(z)$ exists.
3. $\lim_{z \to z_0} f(z) = f(z_0)$.

Condition 3 already contains the first two, since it can only hold if $f(z_0)$ is defined and the limit exists. It can also be written in the $\epsilon$–$\delta$ form: for each positive number $\epsilon$, there is a positive number $\delta$ such that:
$|f(z) - f(z_0)| < \epsilon$ whenever $|z - z_0| < \delta$ (with $z$ in the domain). A function of a complex variable is said to be continuous in a region $R$ if it is continuous at each point of $R$.

A composite of continuous functions is continuous. That is, if $f(z)$ is continuous at $z_0$ and $g(z)$ is continuous at $f(z_0)$, then $g(f(z))$ is continuous at $z_0$. Also, if $f(z)$ and $g(z)$ are continuous at $z_0$ and defined for all $z$ in some neighbourhood $|z - z_0| < \delta$ of $z_0$, then $f(z) + g(z)$, $f(z)g(z)$, and $\frac{f(z)}{g(z)}$ (if $g(z_0) \neq 0$) are also continuous at $z_0$. In view of the above, we can say that a polynomial function is continuous everywhere in the complex plane. A rational function is continuous at all points in its domain.

If a function $f(z)$ is continuous and non-zero at a point $z_0$, then $f(z) \neq 0$ throughout some neighbourhood of $z_0$. This is because if $f(z_0) \neq 0$, then there exists a $\delta > 0$ such that $|f(z) - f(z_0)| < |f(z_0)|$ whenever $|z - z_0| < \delta$. By the triangle inequality, $|f(z)| \geq |f(z_0)| - |f(z) - f(z_0)| > 0$ in that neighbourhood.

Continuity is closely related to the continuity of the real and imaginary parts of a complex function. If $f(z) = u(x, y) + iv(x, y)$, where $u$ and $v$ are real-valued functions of two real variables $x$ and $y$, then $f(z)$ is continuous at $z_0 = x_0 + iy_0$ if and only if both $u(x, y)$ and $v(x, y)$ are continuous at $(x_0, y_0)$. This follows because $|u - u_0|$ and $|v - v_0|$ are each at most $|f(z) - f(z_0)|$, while $|f(z) - f(z_0)| \leq |u - u_0| + |v - v_0|$.

If a function $f(z)$ is continuous on a region $R$ that is both closed and bounded, there exists a non-negative real number $M$ such that $|f(z)| \leq M$ for all $z$ in $R$. This is a consequence of the fact that $|f(z)|$ is a real-valued continuous function, and a real-valued continuous function on a closed and bounded region attains its maximum and minimum values. We can take $M$ to be the maximum value of $|f(z)|$ on $R$.