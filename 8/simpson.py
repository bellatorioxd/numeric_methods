
import math

def rectangle_method(f, a, b, n):
    h = (b-a)/n
    integral = 0
    for i in range(n):
        x = a + (i+0.5)*h
        integral += f(x)
    integral *= h
    return integral

def trapezoid_method(f, a, b, n):
    h = (b-a)/n
    integral = (f(a) + f(b))/2
    for i in range(1, n):
        x = a + i*h
        integral += f(x)
    integral *= h
    return integral

def simpson_method(f, a, b, n):
    h = (b-a)/n
    integral = f(a) + f(b)
    for i in range(1, n):
        x = a + i*h
        if i%2 == 0:
            integral += 2*f(x)
        else:
            integral += 4*f(x)
    integral *= h/3
    return integral

# Example usage
def f(x):
    return math.sin(x)

a = 0
b = math.pi
n = 20

rectangle = rectangle_method(f, a, b, n)
trapezoid = trapezoid_method(f, a, b, n)
simpson = simpson_method(f, a, b, n)

print("Метод прямокутника: {:.9f}".format(rectangle))
print("Метод трапецій: {:.9f}".format(trapezoid))
print("Метод Сімпсона: {:.9f}".format(simpson))

# Calculate error estimates
M2 = 1
M4 = 1
h = (b-a)/n

rectangle_error = M2*h**2*(b-a)/24
trapezoid_error = M2*h**2*(b-a)/12
simpson_error = M4*h**4*(b-a)/2880

print("Похибка за методом прямокутників: {:.9f}".format(rectangle_error))
print("Похибка за методом трапецій: {:.9f}".format(trapezoid_error))
print("Похибка за методом Сімпсона: {:.9f}".format(simpson_error))
