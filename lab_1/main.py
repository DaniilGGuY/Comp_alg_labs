import newton as nw
import hermit as hr
import input as io
import system as stm
import matplotlib.pyplot as plt

db_vals, func_1_vals, func_2_vals, degree_newton, count_hermit, x_searched = io.read_info()

x_coords = list()
y_coords = list()
for i in db_vals:
    x_coords.append(float(i[0]))
    y_coords.append(float(i[1]))

fig, ax = plt.subplots()
ax.plot(x_coords, y_coords)

if len(db_vals) == 0 or len(func_1_vals) == 0 or len(func_2_vals) == 0 or degree_newton < 0 or count_hermit < 1:
    print("Ошибка введенного значения")
else:
    if degree_newton >= len(db_vals):
        print("Степень полинома Ньютона должна быть строго меньше количества узлов в функции")
    else:
        res = nw.calc_result(db_vals, degree_newton, x_searched, 0, 0)
        print("Значение функции вычисленное с помощью полинома Ньютона равно {:5g}".format(res))

    res = nw.calc_result_back(db_vals, 2, 0, 1, 0)
    print("Корень уравнения вычисленный с помощью полинома Ньютона равен {:5g}".format(res))

    if count_hermit >= len(db_vals):
        print("Степень полинома Эрмита должна быть строго меньше количества узлов в функции")
    else:
        res = hr.calc_result(db_vals, count_hermit, x_searched, 0, 0, len(db_vals[0]) - 2)
        print("Значение функции вычисленное с помощью полинома Эрмита равно {:5g}".format(res))

    res = hr.calc_result_back(db_vals, 2, 0, 1, 1, len(db_vals[0]) - 2)
    print("Корень уравнения вычисленный с помощью полинома Эрмита равен {:5g}".format(res))

    func_1_float = list()
    func_2_float = list()
    for i in func_1_vals:
        func_1_float.append([float(i[0]), float(i[1])])
    for i in func_2_vals:
        func_2_float.append([float(i[0]), float(i[1])])

    common = stm.create_system_table(func_1_float, func_2_float)
    res = nw.calc_result_back(common, 3, 0, 1, 0)
    print("Решение системы уравнение, найденное с помощью полинома Ньютона равно {:5g}".format(res))

plt.show()
