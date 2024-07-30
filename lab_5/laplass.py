import math as m

MAX_ITERS = 100
EPS = 1e-6
ITERS = 100

def sympsonFormula(a, b, func):
    return ((b - a) / 6) * (func(a) + 4 * func((a + b) / 2) + func(b))

def sympson(left, right, n, func):
    res = 0.0
    step = (right - left) / n
    for i in range(n):
        res += sympsonFormula(left + i * step, left + (i + 1) * step, func)

    return res

def integral(x):
    return m.exp(-(x ** 2 / 2))

def laplass(x):
    return 2 / m.sqrt(2 * m.pi) * sympson(0, x, ITERS, integral)

def halfDivision(left, right, y, func):
    iter_col = 0
    mid = (left + right) / 2
    while not(abs(func(mid) - y) < EPS or iter_col == MAX_ITERS):
        mid = (left + right) / 2
        if (func(left) - y) * (func(mid) - y) < 0:
            right = mid
        else:
            left = mid
        iter_col += 1

    return mid