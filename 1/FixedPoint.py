"""
Ця функція реалізує ітераційний метод з простою ітерацією для знаходження кореня рівняння.
Функція приймає чотири аргументи: func - це функція, яку ми хочемо вирішити, x0 - початкова точка,
level - максимальна кількість ітерацій, які ми хочемо виконати, та precision - точність, з якою ми хочемо знайти корінь.
Функція повертає корінь рівняння.
"""
def simple_iteration(func, x0, level, precision):
    for i in range(level):
        x1 = func(x0)
        if abs(x1 - x0) < precision:
            return x1
        x0 = x1
    return x1

print("Root of this problem is =", simple_iteration(lambda x: x**2 - 2, 1, 1000, 0.0001))