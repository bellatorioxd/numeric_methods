"""
Цей код реалізує метод Ньютона для знаходження кореня рівняння.
Основна ідея полягає в тому, що на кожному кроці методу проводиться дотична лінія до графіку функції, і тоді корінь шукається як перетин дотичної з віссю абсцис.
Функція newton_method використовується для знаходження кореня рівняння equation з заданою точністю accuracy, починаючи з початкового наближення initial_approximation.
"""


def newton_method(equation, initial_approximation, accuracy):
    x = initial_approximation
    while True:
        fx = equation(x)
        if abs(fx) < accuracy:
            return x
        fprime_x = (equation(x + accuracy) - fx) / accuracy
        x -= fx / fprime_x


def equation(x):
    return x**2 - 2

root = newton_method(equation, 1, 0.0001)
print("Root of this problem is =",root)