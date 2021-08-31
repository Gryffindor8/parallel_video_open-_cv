from scipy.optimize import fsolve
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
import numpy as np


def equations(vars1):
    x1, x2 = vars1

    eq1 = np.cos(x) + 2*np.sin(x) + x2
    eq2 = x**3-5*x1+1
    return [eq1, eq2]


def myFunction(z1):
    x2 = z1[0]
    y2 = z1[1]
    F = np.empty(2)
    F[0] = x2 ** 2 + y2 ** 2 - 20
    F[1] = y2 - x2 ** 2
    return F


zGuess = np.array([1, 1])
z = fsolve(myFunction, zGuess)
print("\nMethod 1:", np.ravel(z))
x, y, z = symbols('x, y, z', real=True)
print("method2:", nonlinsolve([x ** 2 + y ** 2 - 20, y - x ** 2], [x, y]))
