import math
def interpolate(x, y, z):
    n = len(x)
    t = [math.cos((2 * i + 1) * math.pi / (2 * n)) for i in range(n)]

    c = [0] * n
    for j in range(n):
        p = 1
        for k in range(n):
            if k != j:
                p *= (t[j] - t[k]) / (x[j] - x[k])
        c[j] = y[j] * p

    s = 0
    for j in range(n):
        p = 1
        for k in range(n):
            if k != j:
                p *= (z - x[k]) / (x[j] - x[k])
        s += c[j] * p

    return s


x = [math.cos(17 * math.pi / 18),
     math.cos(15 * math.pi / 18),
     math.cos(13 * math.pi / 18),
     math.cos(11 * math.pi / 18),
     math.cos(9 * math.pi / 18),
     math.cos(7 * math.pi / 18),
     math.cos(5 * math.pi / 18),
     math.cos(3 * math.pi / 18),
     math.cos(math.pi / 18)]
y = [0.4448353257,
     0.6012034426,
     0.880798681,
     1.110416785,
     1,
     0.4396349664,
     -0.3180594148,
     -0.9223165206,
     -1.22149625]

x1 = -0.85
x2 = -0.35
x3 = 0.35
x4 = 0.85

p1 = interpolate(x, y, x1)
p2 = interpolate(x, y, x2)
p3 = interpolate(x, y, x3)
p4 = interpolate(x, y, x4)

print("Результат, використовуюючи метод Чебишева для точок  -0.85, -0.35, 0.35, 0.85 :")
print(f"p({x1}) = {p1}")
print(f"p({x2}) = {p2}")
print(f"p({x3}) = {p3}")
print(f"p({x4}) = {p4}")