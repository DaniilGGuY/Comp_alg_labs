triangle_pasc = [ [ 1 ],
                  [1, 1],
                  [1, 2, 1],
                  [1, 3, 3, 1] ]

def fillTrianglePasc(n):
    for i in range(len(triangle_pasc), n + 1):
        new_line = [1]
        for j in range(len(triangle_pasc[i - 1]) - 1):
            new_line.append(triangle_pasc[i - 1][j] + triangle_pasc[i - 1][j + 1])
        new_line.append(1)
        triangle_pasc.append(new_line)

def pascalMat(n, k):
    fillTrianglePasc(n)
    return triangle_pasc[n][k]