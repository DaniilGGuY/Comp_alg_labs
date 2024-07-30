import newton as nw
import input as io
import spline as sp
import numpy as np
import matplotlib.pyplot as plt


filename = "data/test_2.txt"
begin_x, end_x, step_x = -5, 5, 20
begin_y, end_y, step_y = -3, 4, 50
begin_z, end_z, step_z = -1, 2, 30
x_vals = np.linspace(begin_x, end_x, step_x)
y_vals = np.linspace(begin_y, end_y, step_y)
z_vals = np.linspace(begin_z, end_z, step_z)
x_col, y_col, z_col = step_x, step_y, step_z
nx, ny, nz = 3, 2, 5


def draw_table(z_list, y_list, table, x):
    zgrid, ygrid = np.meshgrid(y_list, z_list)
    k = 0
    while (x_vals[k] < x):
        k += 1

    mat = list()
    for i in range(len(z_list)):
        b = list()
        for j in range(len(y_list)):
            b.append(table[i][j][k])
        mat.append(b)

    matgrid = np.asarray(mat)
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    ax.plot_surface(zgrid, ygrid, matgrid, cmap='viridis', edgecolor='green')
    plt.show()


io.file_writer(filename, x_vals, y_vals, z_vals, x_col, y_col, z_col)
func, val_x, val_y, val_z = io.read_info(filename, x_col, y_col, z_col)


mat_nw = list()
mat_sp = list()
for i in range(z_col):
    row_nw = list()
    row_sp = list()
    for j in range(y_col):
        row = list()
        for k in range(x_col):
            row.append([x_vals[k], func[i][j][k]])
        spline = sp.Spline(row, 0, 0)
        row_nw.append(nw.calc_result(row, nx, val_x))
        row_sp.append(spline.calc_value(val_x))
    mat_nw.append(row_nw)
    mat_sp.append(row_sp)

list_nw = list()
list_sp = list()
list_nw_sp = list()
list_sp_nw = list()
for i in range(z_col):
    row_nw = list()
    row_sp = list()
    for j in range(y_col):
        row_nw.append([y_vals[j], mat_nw[i][j]])
        row_sp.append([y_vals[j], mat_sp[i][j]])
    spline_1 = sp.Spline(row_sp, 0, 0)
    spline_2 = sp.Spline(row_nw, 0, 0)
    list_nw.append(nw.calc_result(row_nw, ny, val_y))
    list_sp_nw.append(nw.calc_result(row_sp, ny, val_y))
    list_sp.append(spline_1.calc_value(val_y))
    list_nw_sp.append(spline_2.calc_value(val_y))

row_nw = list()
row_sp = list()
row_nw_sp = list()
row_sp_nw = list()
for i in range(z_col):
    row_nw.append([z_vals[i], list_nw[i]])
    row_sp.append([z_vals[i], list_sp[i]])
    row_sp_nw.append([z_vals[i], list_sp_nw[i]])
    row_nw_sp.append([z_vals[i], list_nw_sp[i]])
spline_1 = sp.Spline(row_nw, 0, 0)
spline_2 = sp.Spline(row_sp, 0, 0)
spline_3 = sp.Spline(row_nw_sp, 0, 0)
spline_4 = sp.Spline(row_sp_nw, 0, 0)
print("Результат для интерполяции ННН: {:5g}".format(nw.calc_result(row_nw, nz, val_z)))
print("Результат для интерполяции ННС: {:5g}".format(spline_1.calc_value(val_z)))
print("Результат для интерполяции НСН: {:5g}".format(nw.calc_result(row_nw_sp, nz, val_z)))
print("Результат для интерполяции НСС: {:5g}".format(spline_3.calc_value(val_z)))
print("Результат для интерполяции СНН: {:5g}".format(nw.calc_result(row_sp_nw, nz, val_z)))
print("Результат для интерполяции СНС: {:5g}".format(spline_4.calc_value(val_z)))
print("Результат для интерполяции ССН: {:5g}".format(nw.calc_result(row_sp, nz, val_z)))
print("Результат для интерполяции ССС: {:5g}".format(spline_2.calc_value(val_z)))
print("Истинное значение функции: {:5g}".format(io.fu(val_x, val_y, val_z)))


draw_table(z_vals, y_vals, func, val_x)

# Test -0.42 1.141 1.43