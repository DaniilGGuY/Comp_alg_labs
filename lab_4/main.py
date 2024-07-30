import approc2d as ap2d
import approc3d as ap3d
import approcHDE as aphde
import input as io
from point import *


def approc2d():
    n = int(input("Введите степень аппроксимирующего полинома: "))
    mat = io.file_reader("data/tmp41.txt")
    table = list()
    for i in range(len(mat)):
        table.append(Point(mat[i][0], mat[i][1], None, mat[i][2]))
    pol_coefs = ap2d.approc(table, n)
    print("Полиномиальные коэффициенты: ", *pol_coefs)
    ap2d.drawApproc(table, pol_coefs)


def approc3d():
    n = 2
    mat = io.file_reader("data/tmp45.txt")
    table = list()
    for i in range(len(mat)):
        table.append(Point(mat[i][1], mat[i][2], mat[i][0], mat[i][3]))
    pol_coefs = ap3d.approc(table, 2)
    print("Полиномиальные коэффициенты: ", *pol_coefs)
    ap3d.drawApproc(table, pol_coefs)


def approcHDE():
    c_coefs_2 = aphde.approc(2)
    print("Полиномиальные коэффициенты для m = 2: ", *c_coefs_2)
    c_coefs_3 = aphde.approc(3)
    print("Полиномиальные коэффициенты для m = 3: ", *c_coefs_3)
    aphde.drawApproc(c_coefs_2, c_coefs_3)


#approc2d()
approc3d()
#approcHDE()
