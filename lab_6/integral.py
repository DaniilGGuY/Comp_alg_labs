from gauss import solveMatrix
from legandre import legandreRoots

def sympsonFormula(a, b, func):
    return ((b - a) / 6) * (func(a) + 4 * func((a + b) / 2) + func(b))


def sympson(left, right, n, func):
    res = 0.0
    step = (right - left) / n
    for i in range(n):
        res += sympsonFormula(left + i * step, left + (i + 1) * step, func)

    return res


def gaussIntagral(a, b, n, integral_func):
    roots = legandreRoots(n)
    x = [(b + a) / 2 + (b - a) / 2 * i for i in roots]
    A_mat = [[roots[j] ** i for j in range(n)] for i in range(n)]
    for i in range(n):
        if i % 2 == 0:
            A_mat[i].append(2 / (i + 1))
        else:
            A_mat[i].append(0)

    coefs = solveMatrix(A_mat)

    sum_calc = 0
    for i in range(n):
        sum_calc += coefs[i] * integral_func(x[i])

    return (b - a) / 2 * sum_calc