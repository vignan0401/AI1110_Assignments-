import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from sympy.abc import x,y 


# Function f(x) defined here
def f(x):
    if (x<=1):
        fval = x*x
        return fval
    else:
        fval = 1/x
        return fval

# Function f'(x) defined here.
def dif(x):
    if (x<=1):
         fval = 2*x
         return fval
    else:
        fval = (-1)/(x*x)
        return fval


x = np.linspace(-2,5,1000)
fvec = np.vectorize(f)
difvec = np.vectorize(dif)
# Two figures are ploted to check continuity and differentiablity of f at x = 1.

plt.figure(1)
plt.plot(x,fvec(x),label='Function is continuous at x = 1')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()


plt.figure(2)
plt.plot(x,difvec(x),label='Function is not differentiable at x = 1')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()


plt.show()
