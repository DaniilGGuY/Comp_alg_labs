def file_reader(filename):
    f = open(filename, "r")
    a = f.readlines()
    b = list()
    f.close()
    for i in a:
        b.append(i.split())

    return b


def read_info():
    f1 = file_reader("data/test.txt")
    f2 = file_reader("data/input_1.txt")
    f3 = file_reader("data/input_2.txt")

    try:
        print("Введите степень полинома Ньютона:")
        degree = int(input())
        print("Введите количество узлов полинома Эрмита:")
        count_h = int(input())
        print("Введите значение, для которого выполняется интерполяция:")
        val_x = float(input())
    except ValueError:
        return [], [], [], -1, -1, -1
    return f1, f2, f3, degree, count_h, val_x
