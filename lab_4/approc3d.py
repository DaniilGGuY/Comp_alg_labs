import math

from slau import solveMatrix
from point import Point
import numpy as np
import matplotlib.pyplot as plt
from math import  exp


def calcCoef(x, y, degx, degy):
    return x ** degx * y ** degy


def makeSlau(table, n):
    coef = list()
    res = list()
    mat = list()

    for i in range(n):
        for j in range(n - i):
            row = list()
            for k in range(n):
                for l in range(n - k):
                    sum_arr = list()
                    for p in table:
                        sum_arr.append(calcCoef(p.x, p.y, k + i, l + j) * p.w)
                    row.append(sum(sum_arr))
            coef.append(row)
            sum_arr = list()
            for p in table:
                sum_arr.append(calcCoef(p.x, p.y, i, j) * p.z * p.w)
            res.append(sum(sum_arr))

    for i in range(len(coef)):
        mat.append(coef[i])
        mat[i].append(res[i])

    return mat


def approc(table, n):
    mat = makeSlau(table, n + 1)
    a_coefs = solveMatrix(mat)

    I = 0.0
    for i in table:
        I += i.w * (i.z - calcZ(a_coefs, i.x, i.y)) ** 2
    print("Ошибка равна: {:5g}".format(I))

    return a_coefs


def calcZ(coefs, x, y):
    z = 0
    k = 0
    n = len(coefs) // 2 - 1
    for i in range(n + 1):
        for j  in range(n + 1 - i):
            z += coefs[k] * calcCoef(x, y, i, j)
            k += 1
    return z


def drawApproc(table, coefs):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    for i in table:
        ax.scatter(i.x, i.y, i.z, c='red')

    x_vals = np.linspace(table[0].x, table[-1].x, len(table) * 3)
    y_vals = np.linspace(table[0].y, table[-1].y, len(table) * 3)
    z_vals = [calcZ(coefs, x_vals[i], y_vals[i]) for i in range(len(x_vals))]

    xgrid, ygrid = np.meshgrid(x_vals, y_vals)
    zgrid = np.array([[calcZ(coefs, xgrid[i][j], ygrid[i][j]) for j in range(len(x_vals))] for i in range(len(y_vals))])
    ax.plot_surface(xgrid, ygrid, zgrid, edgecolor='blue')
    plt.show()
