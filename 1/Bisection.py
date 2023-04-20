"""
Код складається з функції my_bisection,
 яка використовує метод ділення навпіл для знаходження кореня рівняння заданої функції на відрізку [a, b] з заданою точністю precision.
"""

import numpy as np

def my_bisection(func, a, b, precision):
    if np.sign(func(a)) == np.sign(func(b)):
        raise Exception(
            "Рівняння не має коренів")
    midpoint = (a + b) / 2
    if np.abs(func(midpoint)) < precision:
        return midpoint
    elif np.sign(func(a)) == np.sign(func(midpoint)):
        return my_bisection(func, midpoint, b, precision)
    elif np.sign(func(b)) == np.sign(func(midpoint)):
        return my_bisection(func, a, midpoint, precision)



##############################################TEST#######################################
func = lambda x: x**2 - 2

problem = my_bisection(func, 0, 2, 0.01)
print("Root of this problem is =", problem)