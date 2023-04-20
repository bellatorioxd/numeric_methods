def gauss(A, b):
    n = len(A)

    print("System of equations:")
    for i in range(n):
        eq = [f"{A[i][j]}*x{j+1}" for j in range(n)]
        print(" + ".join(eq), f"= {b[i]}")
    print()

    for i in range(n):
        maxrow = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[maxrow][i]):
                maxrow = j

        A[i], A[maxrow] = A[maxrow], A[i]
        b[i], b[maxrow] = b[maxrow], b[i]

        if A[i][i] == 0:
            continue

        for j in range(i+1, n):
            q = A[j][i] / A[i][i]
            A[j][i] = 0
            for k in range(i+1, n):
                A[j][k] -= q * A[i][k]
            b[j] -= q * b[i]



    # Backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        if A[i][i] == 0:
            print("Error: the system has no unique solution")
            return None
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    print("Solution:")
    for i in range(n):
        print(f"x{i+1} = {x[i]}")
    print()

    return x


A = [[1, 0, 0], [0, -5, 0], [0, 0, 1]]
b = [2, 3, 4]
x = gauss(A, b)