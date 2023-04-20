import numpy as np


def square_root(A, b):
    n = len(A)
    L = np.zeros((n, n))
    y = np.zeros(n)

    print("System of equations:")
    for i in range(n):
        eq = [f"{A[i][j]}*x{j + 1}" for j in range(n)]
        print(" + ".join(eq), f"= {b[i]}")
    print()

    for i in range(n):
        for j in range(i):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            L[i][j] = (A[i][j] - s) / L[j][j]
        s = sum(L[i][k] ** 2 for k in range(i))
        temp = A[i][i] - s
        if temp < 0:
            print("No solution")
            return
        L[i][i] = np.sqrt(temp)


    for i in range(n):
        s = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - s) / L[i][i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = sum(L[j][i] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - s) / L[i][i]

    print("Solution:")
    for i in range(n):
        print(f"x{i + 1} = {x[i]}")


A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])
b = np.array([4, 3, 2])
x = square_root(A, b)

