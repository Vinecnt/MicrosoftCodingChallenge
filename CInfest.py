import numpy as np


def make_array(file):
    f = open(file,'r')

    def peek_at_line(f):
        position = f.tell()
        line = f.readline()
        f.seek(position)
        return line

    line_str = peek_at_line(f)
    matrix_len = len(list(line_str)) - 1
    #print(matrix_len)
    arr = np.empty((0, matrix_len), int)

    for line in f:
        return_list = list(line)
        if "\n" in return_list:
            return_list = return_list[:-1]
        arr = np.vstack([arr,return_list])
    return arr

start_arr = make_array("test1.txt")
print(start_arr[1,7])

it = np.nditer(start_arr, flags=['multi_index'])
while not it.finished:
    value = it[0]
    index =  it.multi_index
    value = value.astype(int)
    value = value.flatten()
    value = value[0]

    def left(arr, index_tup):
        if (index[1] != 0):
            if arr[ index_tup[0] ][index_tup[1]]:
                pass
        return False
    it.iternext()
