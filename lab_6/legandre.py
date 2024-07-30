from pascal import pascalMat
from math import cos, pi, sqrt


EPS = 1e-6

def legandrePol(n, x):
    calc_sum = 0
    sign = 1
    for i in range(n // 2 + 1):
        calc_sum += sign * pascalMat(n, i) * pascalMat(2 * (n - i), n) * x ** (n - 2 * i)
        sign *= -1

    return 1 / 2 ** n * calc_sum

def legandrePolDiff(n, x):
    return n / (1 - x ** 2) * (legandrePol(n - 1, x) - x * legandrePol(n, x))

def legandreRoots(n):
    roots = [cos(pi * (4 * i - 1) / (4 * n + 2)) for i in range(n)]
    for i in range(len(roots)):
        while abs(legandrePol(n, roots[i])) > EPS:
            roots[i] -= legandrePol(n, roots[i]) / legandrePolDiff(n, roots[i])

    return roots