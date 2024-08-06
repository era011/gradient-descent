Implemented gradient descent to find the minimum point of a function (surface)

$$z=sin(x)sin(y)$$

from the starting point $(1.2,1.3)$ and the descent of the point itself is shown.

Algorithm:
  1) The starting point $x^0$ is taken randomly.
  2) Find the gradient $\nabla f$, where $\nabla f=(\frac{\partial{f(x,y)}}{\partial x},\frac{\partial{f(x,y)} }{\partial y})$
  3) Find the point of the next iteration $x^{j+1}=x^j-0.01*\nu*\nabla f$
  4) Repeat steps 1-3 the specified number k-times, or until the module displacement of the point $x^j$ is not less than the specified number $\epsilon$

![Graphic](https://github.com/era011/gradient-descent/blob/main/newplot%20(1).png)
