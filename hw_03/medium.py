import numbers

import numpy as np


class StrMixin:
    def __init__(self):
        self.value = None

    def __str__(self):
        return self.value.__str__()


class PrintToFileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__str__())


class FieldsMixin:
    def __init__(self, val):
        self.value = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val


class Matrix(
    np.lib.mixins.NDArrayOperatorsMixin,
    PrintToFileMixin,
    StrMixin,
    FieldsMixin
):
    def __init__(self, value):
        super().__init__()
        self.value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)


if __name__ == '__main__':
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    print(m2)
    (m1 + m2).save_to_file("artifacts/medium/matrix+.txt")
    (m1 * m2).save_to_file("artifacts/medium/matrix*.txt")
    (m1 @ m2).save_to_file("artifacts/medium/matrix@.txt")
