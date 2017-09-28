import numpy as np


def list_maker(file):
    f = open(file,'r')

    def peek_at_line(f):
        position = f.tell()
        line = f.readline()
        f.seek(position)
        return line

    line_str = peek_at_line(f)
    matrix_len = len(line_str.split())

    arr = np.empty((0, matrix_len), int)

    for line in f:
        input_list = line.split()
        return_list = []
        for x in input_list:
            return_list.append(int(x))
        arr = np.vstack([arr,return_list])

    arr = np.transpose(arr)
    for row in arr:
        a = ""
        for x in row:
            a = a + str(x) + " "
        print(a.rstrip())

list_maker("Test_input.txt")


