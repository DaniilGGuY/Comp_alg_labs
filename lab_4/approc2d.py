from slau import solveMatrix
from point import Point
import numpy as np
import matplotlib.pyplot as plt


def makeSlau(table, n):
    mat = [[0.0 for _ in range(n + 1)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            coef = 0
            for k in table:
                coef += k.w * k.x ** (i + j)
            mat[i][j] = coef
        res = 0
        for k in table:
            res += k.w * k.y * k.x ** i
        mat[i][n] = res

    return mat


def approc(table, n):
    mat = makeSlau(table, n + 1)
    a_coefs = solveMatrix(mat)

    I = 0.0
    for i in table:
        I += i.w * (i.y - calcY(a_coefs, i.x)) ** 2
    print("Ошибка равна: {:5g}".format(I))

    return a_coefs


def calcY(coefs, x):
    y = 0
    for i in range(len(coefs)):
        y += coefs[i] * x ** i
    return y


def drawApproc(table, coefs):
    plt.ylabel("Y")
    plt.xlabel("X")

    for i in table:
        plt.plot(i.x, i.y, 'b.')

    x_vals = np.linspace(table[0].x, table[-1].x, len(table) * 10)
    y_vals = [calcY(coefs, x_vals[i]) for i in range(len(x_vals))]

    plt.plot(x_vals, y_vals, 'r')

    plt.show()
