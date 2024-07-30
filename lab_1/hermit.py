EPS = 1e-8


def equal(a, b):
    return abs(a - b) < EPS


def build_dif_table(table, n, x, count_vals):
    dif_table = list()
    der_table = list()
    k = n + 1

    for i in range(k * count_vals):
        dif_table.append([0] * (k * count_vals + 1))
        der_table.append([0] * 2)

    i = 0
    while i < len(table) and float(table[i][0]) < x:
        i += 1

    if i + k // 2 + k % 2 >= len(table):
        left = len(table) - k
        right = len(table)
    else:
        left = max(0, i - k // 2)
        right = left + k

    for i in range(left, right):
        for j in range(count_vals):
            dif_table[(i - left) * count_vals + j][0] = float(table[i][0])
            dif_table[(i - left) * count_vals + j][1] = float(table[i][1])
            der_table[(i - left) * count_vals + j][0] = float(table[i][2])
            der_table[(i - left) * count_vals + j][1] = float(table[i][3])

    for i in range(2, k * count_vals + 1):
        for j in range(k * count_vals + 1 - i):
            if equal(dif_table[j][i - 1], dif_table[j + 1][i - 1]) and i == 2:
                dif_table[j][i] = der_table[j][0]
            elif count_vals == 3 and equal(dif_table[j][i - 1], dif_table[j + 1][i - 1]) and i == 3:
                dif_table[j][i] = der_table[j][1]
            else:
                dif_table[j][i] = (dif_table[j][i - 1] - dif_table[j + 1][i - 1]) / \
                                  (dif_table[j][0] - dif_table[j + i - 1][0])

    return dif_table


def draw_dif_table(table, n, back):
    print(20 * "-" * (n + 2) + "-")
    print("|{:^19}".format("x" if back == 0 else "y"), end='')
    for i in range(n + 1):
        print("|{:^19}".format(("x" if back == 1 else "y") + "{:^1}".format(i)), end='')
    print("|")
    print(20 * "-" * (n + 2) + "-")

    for i in range(n + 1):
        for j in range(n + 2 - i):
            print("|{:^19.5g}".format(table[i][j]), end='')

        for j in range(n + 2 - i, n + 2):
            print("|" + 19 * " ", end='')

        print("|")

    print(20 * "-" * (n + 2) + "-")


def calc_result(table, n, x, mode, is_draw, count_vals):
    dif = build_dif_table(table, n, x, count_vals)
    if is_draw:
        draw_dif_table(dif, n * count_vals + (count_vals - 1), mode)
    res = 0.0
    for i in range(1, (n + 1) * count_vals + 1):
        mult = dif[0][i]
        for j in range(i - 1):
            mult *= (x - dif[j][0])

        res += mult

    return res


def calc_result_back(table, n, x, mode, is_draw, count_vals):
    back_table = list()
    for i in range(len(table)):
        '''der_1 = float(table[i][2])
        der_2 = float(table[i][3])
        if equal(der_1, 0):
            l = float(table[0][0])
            r = float(table[-1][0])
            while abs(r - l) > 1e-3:
                m = (l + r) / 2
                y = calc_result(table, n, m, 0, 0, count_vals)
                if y > x:
                    r = m
                else:
                    l = m

            return l'''
        a = float(table[i][1])
        b = float(table[i][0])
        der_1 = float(table[i][2])
        der_2 = float(table[i][3])
        if equal(der_1, 0):
            if i > 0:
                der_1_1 = (float(table[i - 1][1]) - a) / (float(table[i - 1][0]) - b)
                der_1_2 = (a - float(table[i + 1][1])) / (b - float(table[i + 1][0]))
                der_1 = (der_1_1 + der_1_2) / 2
            else:
                der_1 = float(table[i + 1][2])
            der_2 = -der_2 / (der_1 ** 3)
            der_1 = 1 / der_1
        else:
            der_2 = -der_2 / (der_1 ** 3)
            der_1 = 1 / der_1

        back_table.append([a, b, der_1, der_2])

    return calc_result(back_table, n, x, mode, is_draw, count_vals)
