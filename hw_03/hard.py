import copy

import numpy as np


class HashMixin:
    def __hash__(self):
        return sum(map(sum, self.arr))


class Matrix(HashMixin):
    _cache = {}

    def __init__(self, arr=None, rows=None, cols=None):
        super().__init__()
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
        if self.cols() != o.rows():
            raise Exception("Invalid argument")
        key = (hash(self), hash(o))
        if key not in Matrix._cache:
            res = Matrix(rows=self.rows(), cols=o.cols())
            for i in range(self.rows()):
                for j in range(o.cols()):
                    for k in range(self.cols()):
                        res.arr[i][j] += self.arr[i][k] * o.arr[k][j]
            Matrix._cache[key] = res
        print(Matrix._cache)
        return Matrix._cache[key]

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


if __name__ == '__main__':
    A = Matrix(arr=[[1, 2], [3, 4]])
    B = Matrix(arr=[[1, 0], [0, 1]])
    C = Matrix(arr=[[3, 4], [1, 2]])
    D = Matrix(arr=[[1, 0], [0, 1]])

    A.save_to_file("artifacts/hard/A.txt")
    B.save_to_file("artifacts/hard/B.txt")
    C.save_to_file("artifacts/hard/C.txt")
    D.save_to_file("artifacts/hard/D.txt")

    CD = C @ D
    AB = A @ B
    CD.save_to_file("artifacts/hard/CD.txt")
    AB.save_to_file("artifacts/hard/AB.txt")

    with open("artifacts/hard/hash.txt", 'w') as f:
        f.write(f'{hash(AB)}\n{hash(CD)}')
