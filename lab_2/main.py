import newton as nw
import input as io
import spline as sp
import matplotlib.pyplot as plt
import math as m


db_vals, x_searched = io.read_info()

x_coords = list()
y_coords = list()
for i in db_vals:
    x_coords.append(i[0])
    y_coords.append(i[1])

fig, ax = plt.subplots()
i_vals = list()
table_nw = list()
table_sp_1 = list()
table_sp_2 = list()
table_sp_3 = list()
if len(db_vals) == 0:
    print("Ошибка введенного значения")
else:
    res_newton = nw.calc_result(db_vals, 3, x_searched, 0, 0)
    print("Значение функции, вычисленное с помощью полинома Ньютона равно {:5g}".format(res_newton))

    spline_1 = sp.Spline(db_vals, 0, 0)
    res_spline_1 = spline_1.calc_value(x_searched)
    print("Значение функции, вычисленное с помощью естественного сплайна {:5g}".format(res_spline_1))

    spline_2 = sp.Spline(db_vals, nw.calc_second_deriv(db_vals, db_vals[0][0]), 0)
    res_spline_2 = spline_2.calc_value(x_searched)
    print("Значение функции, вычисленное с помощью сплайна с одной естественной границей {:5g}".format(res_spline_2))

    spline_3 = sp.Spline(db_vals, nw.calc_second_deriv(db_vals, db_vals[0][0]), nw.calc_second_deriv(db_vals, db_vals[-1][0]))
    res_spline_3 = spline_3.calc_value(x_searched)
    print("Значение функции, вычисленное с помощью сплайна без естественных границ {:5g}".format(res_spline_3))

    x_min = db_vals[0][0]
    x_max = db_vals[-1][0]
    step = 0.05
    i = x_min
    while i < x_max:
        i_vals.append(i)
        table_nw.append(nw.calc_result(db_vals, 3, i, 0, 0))
        table_sp_1.append(spline_1.calc_value(i))
        table_sp_2.append(spline_2.calc_value(i))
        table_sp_3.append(spline_3.calc_value(i))
        i += step

ax.plot(i_vals, table_nw, label='Ньютон')
ax.plot(i_vals, table_sp_1, label='Сплайн 1')
ax.plot(i_vals, table_sp_2, label='Сплайн 2')
ax.plot(i_vals, table_sp_3, label='Сплайн 3')
ax.legend()

plt.show()

