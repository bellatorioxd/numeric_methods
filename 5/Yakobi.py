import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = x0
    for i in range(max_iter):
        x_prev = x
        x = (b - np.dot(R, x)) / D
        if np.linalg.norm(x - x_prev) < tol:
            return x, i+1

A = np.array([[25.0, 10.00, -7.50], [10.00, 29.00, -8.00], [-7.50, -8.00, 28.25]])
b = np.array([60.00, 84.00, -80.00])
x0 = np.array([1.0, 1.0, 1.0])

approx_solution, num_iterations = jacobi(A, b, x0, tol=0.001, max_iter=1000)
print("Approximate solution:", approx_solution)
print("Number of iterations:", num_iterations)



