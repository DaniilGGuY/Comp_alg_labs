from input import file_reader
import differ as dif
from spline import spline3d
from integral import gaussIntagral, sympson
from math import log, exp

XITERS = 10
YITERS = 10

def task1():
    z = file_reader("data/test.txt")
    x = [ i / 10 for i in range(len(z)) ]
    y = [ i / 10 for i in range(len(z)) ]
    z_leveling = [[log(z[j][i]) for i in range(len(x))] for j in range(len(y))]

    func = spline3d(x, y, z)
    func_leveling = spline3d(x, y, z_leveling)

    def integralYFunc(y_):
        def integral_func(x_):
            return func(x_, y_)
        return gaussIntagral(0, 1 - y_, YITERS, integral_func)

    def integralYFuncLeveling(y_):
        def integral_func(x_):
            return exp(func_leveling(x_, y_))
        return gaussIntagral(0, 1 - y_, YITERS, integral_func)

    res = sympson(0, 1, XITERS, integralYFunc)
    print("Двукратный интеграл табличной функции равен: ", res)
    res_leveling = sympson(0, 1, XITERS, integralYFuncLeveling)
    print("Двукратный интеграл табличной функции равен с выравниванием: ", res_leveling)

# --------------------------------------- Доп
    def func(x, y):
        return x ** 2 + y ** 2

    innerIntegralFunc = lambda x: gaussIntagral(x ** 2, x, YITERS, lambda y: func(x, y))

    res = sympson(0, 1, XITERS, innerIntegralFunc)
    print("Двукратный интеграл (доп): ", res)



def task2():
    x = [1, 2, 3, 4, 5, 6]
    y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]
    oneSide = dif.oneSideDiffDDiffer(x, y)
    centralSide = dif.twoSideDiffDDiffer(x, y)
    runge = dif.secondRungeFormulaDifferCentral(x, y)
    leveling = dif.levelingVariablesDiffer(x, y)
    secondDif = dif.secondDiffDiffer(x, y)
    for i in range(len(x)):
        print("{:.5f} {:.5f} {:.5f} {:.5f} {:.5f} {:.5f} {:.5f}".format(x[i], \
                y[i], oneSide[i], centralSide[i], runge[i], leveling[i], secondDif[i]))

task1()
#task2()
