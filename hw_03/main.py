import numpy as np

from easy import Matrix

if __name__ == '__main__':
    np.random.seed(0)
    m1 = Matrix(arr=np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(arr=np.random.randint(0, 10, (10, 10)))
    (m1 + m2).save_to_file("artifacts/easy/matrix+.txt")
    (m1 * m2).save_to_file("artifacts/easy/matrix*.txt")
    (m1 @ m2).save_to_file("artifacts/easy/matrix@.txt")
