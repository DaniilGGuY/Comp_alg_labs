def calc_ksi(ksi_i, h_i, h_i_1):
    return -h_i / (2 * (h_i + h_i_1) + h_i_1 * ksi_i)


def calc_etta(dy_i, dy_i_1, h_i, h_i_1, etta_i, ksi_i):
    return (3 * (dy_i / h_i - dy_i_1 / h_i_1) - h_i_1 * etta_i) / (h_i_1 * ksi_i + 2 * (h_i + h_i_1))


class Spline:
    def __init__(self, table, first, last):
        self.table = table
        self.a_coef = self.calc_a()
        self.c_coef = self.calc_c(first, last)
        self.b_coef = self.calc_b(first, last)
        self.d_coef = self.calc_d(first, last)

    def calc_a(self):
        a = [0] * (len(self.table) - 1)
        for i in range(len(self.table) - 1):
            a[i] = self.table[i][1]

        return a

    def calc_b(self, first, last):
        b = [0] * (len(self.table) - 1)

        for i in range(len(self.table) - 2):
            h_i = self.table[i + 1][0] - self.table[i][0]
            dy_i = self.table[i + 1][1] - self.table[i][1]
            b[i] = dy_i / h_i - 1 / 3 * h_i * (self.c_coef[i + 1] + 2 * self.c_coef[i])

        h_N = self.table[-1][0] - self.table[-2][0]
        dy_N = self.table[-1][1] - self.table[-2][1]
        b[-1] = dy_N / h_N - 1 / 3 * h_N * ((last / 2) + 2 * self.c_coef[-1])

        return b

    def calc_c(self, first, last):
        c = [0] * (len(self.table) - 1)
        ksi = [0] * (len(self.table))
        etta = [0] * (len(self.table))

        c[0] = first / 2
        ksi[1] = 0
        etta[1] = first / 2

        for i in range(2, len(self.table)):
            h_i = self.table[i][0] - self.table[i - 1][0]
            h_i_1 = self.table[i - 1][0] - self.table[i - 2][0]
            ksi[i] = calc_ksi(ksi[i - 1], h_i, h_i_1)
            dy_i = self.table[i][1] - self.table[i - 1][1]
            dy_i_1 = self.table[i - 1][1] - self.table[i - 2][1]
            etta[i] = calc_etta(dy_i, dy_i_1, h_i, h_i_1, etta[i - 1], ksi[i - 1])

        c[-1] = etta[-1] + (last / 2) * ksi[-1]

        for i in range(len(self.table) - 2, 0, -1):
            c[i - 1] = etta[i] + c[i] * ksi[i]

        return c

    def calc_d(self, first, last):
        d = [0] * (len(self.table) - 1)

        for i in range(len(self.table) - 2):
            h_i = self.table[i + 1][0] - self.table[i][0]
            d[i] = (self.c_coef[i + 1] - self.c_coef[i]) / (3 * h_i)

        h_N = self.table[-1][0] - self.table[-2][0]
        d[-1] = ((last / 2) - self.c_coef[-1]) / (3 * h_N)

        return d

    def calc_value(self, x):
        i = 0
        while i < len(self.table) - 2 and x > self.table[i + 1][0]:
            i += 1

        x_i = self.table[i][0]
        dx = x - x_i

        return self.a_coef[i] + dx * self.b_coef[i] + self.c_coef[i] * dx ** 2 + self.d_coef[i] * dx ** 3
