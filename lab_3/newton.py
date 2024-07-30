def build_dif_table(table, n, x):
    dif_table = list()
    k = n + 1

    for i in range(k):
        dif_table.append([0] * (k + 1))

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
        dif_table[i - left][0] = float(table[i][0])
        dif_table[i - left][1] = float(table[i][1])

    for i in range(2, k + 1):
        for j in range(k + 1 - i):
            dif_table[j][i] = (dif_table[j][i - 1] - dif_table[j + 1][i - 1]) / \
                              (dif_table[j][0] - dif_table[j + i - 1][0])

    return dif_table


def calc_result(table, n, x):
    dif = build_dif_table(table, n, x)

    res = 0.0
    for i in range(1, n + 2):
        mult = dif[0][i]
        for j in range(i - 1):
            mult *= (x - dif[j][0])

        res += mult

    return res
