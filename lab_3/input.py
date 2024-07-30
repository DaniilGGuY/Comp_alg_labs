import numpy as np

def fu(x, y, z):
    return np.exp(2 * x - y) * z ** 3

def file_reader(filename, x, y, z):
    f = open(filename, "r")
    a = f.readlines()
    f.close()

    func = list()
    for i in range(z):
        b = list()
        for j in range(y):
            b.append(list(map(float, a[i * y + j].split())))
        func.append(b)

    return func

def file_writer(filename, x_vals, y_vals, z_vals, x, y, z):
    f = open(filename, "w")
    for i in range(z):
        for j in range(y):
            b = ""
            for k in range(x):
                b += str(fu(x_vals[k], y_vals[j], z_vals[i])) + " "
            f.write(b + '\n')
    f.close()

def read_info(filename, x, y, z):
    try:
        func = file_reader(filename, x, y, z)
        val_x, val_y, val_z = map(float, input("Введите значение, для которого выполняется интерполяция: ").split())
    except ValueError:
        return [], -1, -1, -1
    except IndexError:
        return [], -1, -1, -1
    return func, val_x, val_y, val_z
