import newton as nw


def create_system_table(func_1_vals, func_2_vals):
    func_1_vals.sort()
    func_2_vals.sort()
    func_common = list()
    i = 0
    j = 0
    while i < len(func_2_vals) or j < len(func_1_vals):
        if j == len(func_1_vals):
            y = nw.calc_result(func_1_vals, 4, func_2_vals[i][0], 0, 0)
            func_1_vals.append([func_2_vals[i][0], y])
        elif i == len(func_2_vals):
            y = nw.calc_result(func_2_vals, 4, func_1_vals[j][0], 0, 0)
            func_2_vals.append([func_1_vals[j][0], y])
        elif func_1_vals[j][0] < func_2_vals[i][0]:
            y = nw.calc_result(func_2_vals, 4, func_1_vals[j][0], 0, 0)
            func_2_vals.insert(i, [func_1_vals[j][0], y])
        elif func_1_vals[j][0] >= func_2_vals[i][0]:
            y = nw.calc_result(func_1_vals, 4, func_2_vals[i][0], 0, 0)
            func_1_vals.insert(j, [func_2_vals[i][0], y])
        i += 1
        j += 1

    for i in range(len(func_1_vals)):
        func_common.append([func_1_vals[i][0], func_1_vals[i][1] - func_2_vals[i][1]])

    func_common.sort()

    left = right = 0
    for i in range(len(func_common) - 1):
        if func_common[i][1] < 0:
            left = i - 2
            right = i + 2
            break

    return func_common[left:right]
