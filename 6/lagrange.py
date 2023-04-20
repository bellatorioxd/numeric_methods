"""
lagrange_interpolation приймає значення x та y у вигляді масивів інтерполяційних точок, а також значення x_val, у які виконується інтерполяція.
У циклі змінна L обчислюється як добуток усіх доданків (x_val - x[j]) / (x[i] - x[j]), де j ≠ i.
Кожен L домножується на відповідне значення y, після чого сумується.
Ця сума і є результатом інтерполяції.
"""
import numpy as np


def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x_val - x[j]) / (x[i] - x[j])
        result += y[i] * L
    return result



x = np.array([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75 ,1])
y = np.array([0.4253241483, 0.7523759617, 1.019727844, 1.124986521, 1, 0.6301786026, 0.0608767673, -0.6109015583, -1.257617821])

x_vals = np.array([-0.85, -0.35, 0.35, 0.85])

lagrange_results = [lagrange_interpolation(x, y, x_val) for x_val in x_vals]

print("Результат, використовуюючи метод Лагранжа для точок  -0.85, -0.35, 0.35, 0.85 :")
for i, x_val in enumerate(x_vals):
    print(f"L({x_val}) = {lagrange_results[i]}")

