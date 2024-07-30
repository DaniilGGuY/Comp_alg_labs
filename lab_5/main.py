import numpy as np
import matplotlib.pyplot as plt
from newton import newtonMethod
from laplass import laplass, halfDivision
import math as m

def task1():
    def func1(x, y, z):
        return x ** 2 + y ** 2 + z ** 2 - 1

    def func2(x, y, z):
        return 2 * x ** 2 + y ** 2 - 4 * z

    def func3(x, y, z):
        return 3 * x ** 2 - 4 * y + z ** 2

    def jacobi(x, y, z):
        return [[2 * x, 2 * y, 2 * z],
                [4 * x, 2 * y, -4],
                [6 * x, -4, 2 * z]]

    x_beg, y_beg, z_beg = 1, 1, 1

    x, y, z = newtonMethod([func1, func2, func3], jacobi, [x_beg, y_beg, z_beg])

    print(f'Решение системы: \nx = {x} \ny = {y} \nz = {z}')
    print(f'Значение функций: \nfunc1 = {func1(x, y, z)}')
    print(f'func2 = {func2(x, y, z)}')
    print(f'func3 = {func3(x, y, z)}')

def task2():
    left, right = -5, 5
    x_real = np.linspace(left, right, 100)
    y_real = [laplass(i) for i in x_real]

    f_val = float(input("Введите значение функции: "))
    x_calculated = halfDivision(left, right, f_val, laplass)
    print("Значение аргумента: ", x_calculated)
    print("Значение функции при найденном значении аргумента: ", laplass(x_calculated))

    fig, ax = plt.subplots()
    ax.plot(x_real, y_real)
    ax.plot(x_calculated, f_val, 'r.')
    plt.show()

def task3():
    x0, y0, x1, y1 = 0, 1, 1, 3
    n = 100
    step = (x1 - x0) / n
    x = np.linspace(x0, x1, n + 1)

    def jacobi(*y):
        n = len(y)
        res = list()
        res.append([1] + [0] * (n - 1))
        for i in range(1, n - 1):
            res.append([0] * (i - 1) + [1 / step ** 2] + [-2 / step ** 2 - 3 * (y[i] + x[i] ** 3) ** 2] + [1 / step ** 2] + [0] * (n - i - 2))
        res.append([0] * (n - 1) + [1])
        return res

    def createFuncs(num):
        if num == 0:
            def func(*y):
                return y[0] - y0
        elif num == n:
            def func(*y):
                return y[num] - y1
        else:
            def func(*y):
                return (y[num - 1] - 2 * y[num] + y[num + 1]) / step ** 2 - (y[num] + x[num] ** 3) ** 2
        return func

    funcs = [createFuncs(i) for i in range(n + 1)]

    y = [ (i * i + i + 1) for i in x]

    res = newtonMethod(funcs, jacobi, y)
    arg = -2
    print("Начальное приближение: ", y[arg])
    print("Найденное значение", res[arg])
    fig, ax = plt.subplots()
    ax.plot(x, res)
    plt.show()


# task1()
# task2()
task3()
