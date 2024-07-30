import numpy as np
from gauss import solveMatrix

def coefs(x, y):
    x = np.array(x)
    y = np.array(y)

    deltaX = np.diff(x)
    deltaY = np.diff(y)

    A = np.zeros((len(x), len(x)))
    B = np.zeros(len(x))
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, len(x) - 1):
        A[i, i - 1] = deltaX[i - 1]
        A[i, i] = 2 * (deltaX[i - 1] + deltaX[i])
        A[i, i + 1] = deltaX[i]
        B[i] = 3 * ((deltaY[i] / deltaX[i]) - (deltaY[i - 1] / deltaX[i - 1]))

    C = A
    C = C.tolist()
    for i in range(len(B)):
        C[i].append(B[i])
    C = np.array(solveMatrix(C))

    B = np.zeros(len(x) - 1)
    D = np.zeros(len(x) - 1)
    A = np.zeros(len(x) - 1)

    for i in range(0, len(x) - 1):
        D[i] = (C[i + 1] - C[i]) / (3 * deltaX[i])
        B[i] = (deltaY[i] / deltaX[i]) - (deltaX[i] / 3) * (2 * C[i] + C[i + 1])
        A[i] = y[i]

    return A, B, C, D


def spline(x, y):
    A, B, C, D = coefs(x, y)

    def func(x0):
        x_cur = 0
        if x0 < x[0]:
            x_cur = 0
        else:
            for i in range(1, len(x)):
                if x0 < x[i]:
                    x_cur = i - 1
                    break
            else:
                x_cur = len(x) - 2
        return A[x_cur] + (x0 - x[x_cur]) * B[x_cur] + (x0 - x[x_cur]) ** 2 * C[x_cur] + (x0 - x[x_cur]) ** 3 * D[x_cur]

    return func


def spline3d(x, y, z):
    funcs = []
    for j in range(len(y)):
        funcs.append(spline(x, [z[j][i] for i in range(len(x))]))

    def func(x0, y0):
        z0 = []
        for j in range(len(y)):
            z0.append(funcs[j](x0))
        return spline(y, z0)(y0)

    return func