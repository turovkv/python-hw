import copy

import numpy as np


class Matrix:
    def __init__(self, arr=None, rows=None, cols=None):
        if arr is not None:
            self.arr = copy.deepcopy(arr)
        else:
            self.arr = [[0] * cols for r in range(rows)]

    def rows(self):
        return len(self.arr)

    def cols(self):
        return len(self.arr[0])

    def __add__(self, o):
        if self.rows() != o.rows() or self.cols() != o.cols():
            raise Exception("Invalid argument")
        res = Matrix(rows=self.rows(), cols=self.cols())
        for i in range(self.rows()):
            for j in range(self.cols()):
                res.arr[i][j] = self.arr[i][j] + o.arr[i][j]
        return res

    def __mul__(self, o):
        if self.rows() != o.rows() or self.cols() != o.cols():
            raise Exception("Invalid argument")
        res = Matrix(rows=self.rows(), cols=self.cols())
        for i in range(self.rows()):
            for j in range(self.cols()):
                res.arr[i][j] = self.arr[i][j] * o.arr[i][j]
        return res

    def __matmul__(self, o):
        np.array([5, 6]) @ np.array([5, 6])
        if self.cols() != o.rows():
            raise Exception("Invalid argument")
        res = Matrix(rows=self.rows(), cols=o.cols())
        for i in range(self.rows()):
            for j in range(o.cols()):
                for k in range(self.cols()):
                    res.arr[i][j] += self.arr[i][k] * o.arr[k][j]
        return res

    def __str__(self):
        s = ""
        for r in self.arr:
            for c in r:
                s += str(c)
                s += ' '
            s += '\n'
        return s

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__str__())
