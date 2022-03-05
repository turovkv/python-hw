import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import reduce


def get_fib_list(n: int):
    mod = 1e9 + 7
    fib_list = [1, 1]
    while len(fib_list) < n:
        fib_list.append((fib_list[-1] + fib_list[-2]) % mod)
    return fib_list


N = 10
arg_list = [8 * 10 ** 6] * 10


def calc_multi_thread():
    start = time.time()
    with ThreadPoolExecutor(max_workers=N) as executor:
        res = reduce(
            lambda a, b: a + b,
            map(lambda a: a[-1], executor.map(get_fib_list, arg_list))
        )
    end = time.time()
    return f'calc_multi_thread time={end - start}, res={res}\n'


def calc_multi_process():
    start = time.time()
    with ProcessPoolExecutor(max_workers=N) as executor:
        res = reduce(
            lambda a, b: a + b,
            map(lambda a: a[-1], executor.map(get_fib_list, arg_list))
        )
    end = time.time()
    return f'calc_multi_process time={end - start}, res={res}\n'


def calc_sync():
    start = time.time()
    res = sum(map(lambda a: a[-1], map(get_fib_list, arg_list)))
    end = time.time()
    return f'calc_sync time={end - start}, res={res}\n'


if __name__ == '__main__':
    with open("artifacts/easy.txt", 'w') as f:
        f.write(calc_sync())
        f.write(calc_multi_thread())
        f.write(calc_multi_process())
