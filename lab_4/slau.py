def toTriangleMatrix(mat):
    n = len(mat)
    for k in range(n - 1):
        for i in range(k + 1, n):
            coef = -(mat[i][k] / mat[k][k])
            for j in range(k, n + 1):
                mat[i][j] += coef * mat[k][j]

    return mat


def solveMatrix(mat):
    mat = toTriangleMatrix(mat)
    n = len(mat)

    solve = [0.0] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            mat[i][n] -= solve[j] * mat[i][j]

        try:
            solve[i] = mat[i][n] / mat[i][i]
        except:
            return None

    return solve
