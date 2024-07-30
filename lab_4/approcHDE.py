from slau import solveMatrix
from point import Point
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfi

def trueRes(x):
    return ((-(np.exp(0.5) + 1) / erfi(1 / np.sqrt(2))) * erfi(x / np.sqrt(2)) + 1) / np.exp(x ** 2 / 2) + x


def u0(x):
    return 1 - x


def u1(x):
    return x * (1 - x)


def u2(x):
    return x ** 2 * (1 - x)


def u3(x):
    return x ** 3 * (1 - x)


def c0(x):
    return 1 - 4 * x


def c1(x):
    return -2 + 2 * x - 3 * x ** 2


def c2(x):
    return 2 - 6 * x + 3 * x ** 2 - 4 * x ** 3


def c3(x):
    return 6 * x - 12 * x ** 2 + 4 * x ** 3 - 5 * x ** 4


def res(x):
    return 2 * x


u = [u0, u1, u2, u3]
c = [c0, c1, c2, c3]


def makeSlau(table, n):
    mat = [[0.0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            coef = 0
            for k in table:
                coef += c[i + 1](k) * c[j + 1](k)
            mat[i][j] = coef
        val = 0
        for k in table:
            val += c[0](k) * c[i + 1](k)
        mat[i][n] = -val

    return mat


def approc(n):
    x = np.linspace(0, 9, 2 * n)
    mat = makeSlau(x, n)
    c_coefs = solveMatrix(mat)
    return c_coefs


def calcY(coefs, x):
    y = 0
    for i in range(len(coefs)):
        y += coefs[i] * u[i + 1](x)
    return y + u[0](x)


def drawApproc(coefs_2, coefs_3):
    plt.ylabel("Y")
    plt.xlabel("X")


    x_vals = np.linspace(0, 1, 100)
    y_vals_2 = [calcY(coefs_2, x_vals[i]) for i in range(len(x_vals))]
    y_vals_3 = [calcY(coefs_3, x_vals[i]) for i in range(len(x_vals))]
    y_vals_true = [trueRes(x_vals[i]) for i in range(len(x_vals))]

    plt.plot(x_vals, y_vals_2, 'r', label="m=2")
    plt.plot(x_vals, y_vals_3, 'b', label="m=3")
    plt.plot(x_vals, y_vals_true, 'g', label="Истинное значение")

    plt.legend()
    plt.show()
