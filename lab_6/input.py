def file_reader(filename):
    f = open(filename, "r")
    mat = [ list(map(float, i.split())) for i in f.readlines() ]
    f.close()
    return mat
