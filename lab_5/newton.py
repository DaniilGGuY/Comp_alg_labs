from gauss import solveMatrix

MAX_ITERS = 100
EPS = 1e-6

def calcVal(funcs, vals):
    return [f(*vals) for f in funcs]

def createMatrix(funcs, jacobi, vals):
    ans = calcVal(funcs, vals)
    mat = jacobi(*vals)
    for i in range(len(ans)):
        mat[i].append(-ans[i])

    return mat

def calcNewIterVals(prev, diff):
    return [prev[i] + diff[i] for i in range(len(prev))]

def newtonMethod(funcs, jacobi, beg_vals):
    iter_vals, iter_col = beg_vals, 1
    while True:
        diff = solveMatrix(createMatrix(funcs, jacobi, iter_vals))
        iter_vals = calcNewIterVals(iter_vals, diff)
        if iter_col == MAX_ITERS or sum([val ** 2 for val in diff]) ** 0.5 < EPS:
            break
        iter_col += 1

    return iter_vals
