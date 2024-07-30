def file_reader(filename):
    f = open(filename, "r")
    a = f.readlines()
    b = list()
    mat = list()
    f.close()
    for i in a:
        b.append(i.split())

    for i in b:
        mat.append([float(i[0]), float(i[1])])

    mat.sort()

    return mat


def read_info():
    f1 = file_reader("data/test.txt")

    try:
        print("Введите значение, для которого выполняется интерполяция:")
        val_x = float(input())
    except ValueError:
        return [], -1
    return f1, val_x
