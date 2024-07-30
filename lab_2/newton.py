def build_dif_table(table, n, x):
    dif_table = list()
    k = n + 1

    for i in range(k):
        dif_table.append([0] * (k + 1))

    i = 0
    while i < len(table) and table[i][0] < x:
        i += 1

    if i + k // 2 + k % 2 >= len(table):
        left = len(table) - k
        right = len(table)
    else:
        left = max(0, i - k // 2)
        right = left + k

    for i in range(left, right):
        dif_table[i - left][0] = table[i][0]
        dif_table[i - left][1] = table[i][1]

    for i in range(2, k + 1):
        for j in range(k + 1 - i):
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


def calc_result(table, n, x, mode, is_draw):
    dif = build_dif_table(table, n, x)
    if is_draw:
        draw_dif_table(dif, n, mode)
    res = 0.0
    for i in range(1, n + 2):
        mult = dif[0][i]
        for j in range(i - 1):
            mult *= (x - dif[j][0])

        res += mult

    return res


def calc_result_back(table, n, x, mode, is_draw):
    back_table = list()
    for i in range(len(table)):
        a = table[i][1]
        b = table[i][0]
        back_table.append([a, b])

    return calc_result(back_table, n, x, mode, is_draw)


def calc_second_deriv(table, x):
    dif = build_dif_table(table, 3, x)
    return 2 * dif[0][3] + (6 * x - 2 * (dif[0][0] + dif[1][0] + dif[2][0])) * dif[0][4]

