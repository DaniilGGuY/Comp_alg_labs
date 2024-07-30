def oneSideDiffDDiffer(x, y):
    diff = list()
    for i in range(len(y) - 1):
        diff.append((y[i + 1] - y[i]) / (x[i + 1] - x[i]))
    diff.append(diff[-1])
    return diff


def twoSideDiffDDiffer(x, y):
    diff = list()
    diff.append((-3 * y[0] + 4 * y[1] - y[2]) / (2 * (x[1] - x[0])))
    for i in range(1, len(y) - 1):
        diff.append((y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1]))
    diff.append((y[-3] - 4 * y[-2] + 3 * y[-1]) / (2 * (x[-1] - x[-2])))
    return diff


def secondRungeFormulaDiffer(x, y):
    diff = list()
    for i in range(len(y) - 2):
        diff.append((4 * y[i + 1] - 3 * y[i] - y[i + 2]) / (x[i + 2] - x[i]))
    diff.append((3 * y[-2] + y[-4] - 4 * y[-3]) / (x[-2] - x[-4]))
    diff.append((3 * y[-1] + y[-3] - 4 * y[-2]) / (x[-1] - x[-3]))
    return diff


def secondRungeFormulaDifferCentral(x, y):
    diff = list()
    for i in range(2, len(y) - 2):
        y1 = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
        y2 = (y[i + 2] - y[i - 2]) / (x[i + 2] - x[i - 2])
        diff.append(y1 + (y1 - y2) / 3)
    diff.insert(0, diff[0])
    diff.insert(0, diff[0])
    diff.append(diff[-1])
    diff.append(diff[-1])

    return diff


def levelingVariablesDiffer(x, y):
    diff = list()
    for i in range(len(y) - 1):
        diff.append((x[i + 1] / y[i + 1]) * ((y[i + 1] - y[i]) * (x[i + 1] - x[i])) * (y[i] / x[i]))
    diff.append((x[-1] / y[-1]) * ((y[-1] - y[-2]) * (x[-1] - x[-2])) * (y[-2] / x[-2]))
    return diff


def secondDiffDiffer(x, y):
    diff = list()
    diff.append((y[0] - 2 * y[1] + y[2]) / (x[1] - x[0]) ** 2)
    for i in range(1, len(y) - 1):
        diff.append((y[i - 1] - 2 * y[i] + y[i + 1]) / (x[i] - x[i - 1]) ** 2)
    diff.append((y[-3] - 2 * y[-2] + y[-1]) / (x[-2] - x[-3]) ** 2)
    return diff
