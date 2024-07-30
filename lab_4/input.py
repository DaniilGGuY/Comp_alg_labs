def file_reader(filename):
    f = open(filename, "r")
    a = f.readlines()
    b = list()
    f.close()
    for i in a:
        b.append(list(map(float, i.split())))
    return b