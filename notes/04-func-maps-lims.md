<!-- title: Functions, Mappings and Limits -->
<!-- order: 4 -->

## Functions of a Complex Variable

A function in mathematics is a definition/rule that assigns a unique output to each input. That's no different in the context of complex numbers. A function of a complex variable is a rule that assigns a complex number $w$ to each complex number $z$ in a defined domain. We can write this as $w = f(z)$, where $f$ is the function, $z$ is the input complex number, and $w$ is the output complex number.

Given $z = x + iy$ and $w = u + iv$, we can write the function as $f(z) = f(x + iy) = u + iv$. Here $u$ and $v$ are real-valued functions of $x$ and $y$, so the function becomes: $f(x + iy) = u(x, y) + i\,v(x, y)$.

In polar form, we can write the function as $f(z) = f(re^{i\theta}) = u + iv$. Here $u$ and $v$ are functions of $r$ and $\theta$, so the function becomes: $f(re^{i\theta}) = u(r, \theta) + i\,v(r, \theta)$.

A few things to note:
- The domain of a function is the set of all possible input values for which the function is defined. In the case of complex functions, the domain is a subset of the complex plane. It is also called the domain of definition.
- The range of a function is the set of all possible output values that the function can produce. In the case of complex functions, the range is also a subset of the complex plane.
- The function needs to be well-defined, meaning for each input value in the domain, there should be a unique output value.
- When the domain of definition is not mentioned, it is assumed to be the largest possible domain for which the function is defined. For example, the function $f(z) = \frac{1}{z}$ is defined for all complex numbers except $z = 0$. Therefore, its domain of definition is $\mathbb{C} \setminus \{0\}$.

### Mappings

Functions can be visualized to understand how they transform the input values to output values. This is fairly easy to visualize for functions where only two axes are involved. For example, consider a function $f(x) = x^2$ that maps real numbers to real numbers. We can visualize this function by plotting the input values on the x-axis and the corresponding output values on the y-axis.

For functions of complex numbers, however, we have four axes to consider: the real and imaginary parts of the input complex number, and the real and imaginary parts of the output complex number. This makes it hectic to visualize the function in a single plot. However, with mapping, we can visualize the transformation by considering the input and output complex numbers as points in their own complex planes.

In the diagram below, the graph of the function would need 4 dimensions ($\mathbb{R}^2 \times \mathbb{R}^2$), which we cannot draw. Instead, we draw the input plane and the output plane side by side, and see how points (and curves) in the input plane are carried to the output plane.

<!-- figure: 04-plot-1 -->
<!-- code: 04-plot-1 -->

### Limits

The concept of limits, as known in calculus, can be extended to functions of complex variables. With complex functions, a defined neighbourhood around a point in the complex plane is considered. The function must be defined in a punctured neighbourhood of $z_0$, that is, a neighbourhood with $z_0$ itself removed, because the value of $f$ at $z_0$ plays no part in the limit.

The limit of a function $f(z)$ as $z$ approaches a point $z_0$ is denoted as $\lim_{z \to z_0} f(z)$. This limit exists if, for every sequence of complex numbers $\{z_n\}$ with $z_n \neq z_0$ that converges to $z_0$, the corresponding sequence of function values $\{f(z_n)\}$ converges to the same value $L$. In other words, the limit exists if the function approaches the same value from all directions in the complex plane as $z$ approaches $z_0$.

By the definition of limits, we can say that the limit of a function $f(z)$ as $z$ approaches a point $z_0$ is equal to $L$ if, for every $\epsilon > 0$, there exists a $\delta > 0$ such that whenever $0 < |z - z_0| < \delta$, it follows that $|f(z) - L| < \epsilon$. This means that we can make the function values arbitrarily close to $L$ by choosing input values sufficiently close to $z_0$.

### Theorems on limits

- **Definition:** $f(z)$ is continuous at $z_0$ if $f(z_0)$ is defined and $\lim_{z \to z_0} f(z) = f(z_0)$.

- **Theorem 1:** If $\lim_{z \to z_0} f(z) = L$ and $\lim_{z \to z_0} g(z) = M$, then:
  - $\lim_{z \to z_0} [f(z) + g(z)] = L + M$
  - $\lim_{z \to z_0} [f(z)g(z)] = LM$
  - $\lim_{z \to z_0} \frac{f(z)}{g(z)} = \frac{L}{M}$, provided $M \neq 0$

- **Theorem 2:** If $f(z)$ is continuous at $z_0$ and $g(z)$ is continuous at $f(z_0)$, then the composition $g(f(z))$ is continuous at $z_0$.
