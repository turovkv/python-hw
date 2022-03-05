import math
import os
import time
from concurrent.futures import ProcessPoolExecutor


class Arg:
    def __init__(self, f, a, b, n_iter, log=None):
        self.f = f
        self.a = a
        self.b = b
        self.n_iter = n_iter
        self.log = log


def integrate(arg: Arg):
    f, a, b, n_iter, log = arg.f, arg.a, arg.b, arg.n_iter, arg.log
    start = time.time()
    if log:
        print(
            f"start integrate (f, a={a}, b={b}, n_iter={n_iter})"
            f" with process {os.getpid()}"
        )
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    end = time.time()
    if log:
        print(
            f"end integrate (f, a={a}, b={b}, n_iter={n_iter})"
            f" with process {os.getpid()}, time={end - start}"
        )
    return acc


def integrate_mp(f, a, b, n_jobs=1, n_iter=3* 10 ** 8, log=None, log_exp=None):
    start = time.time()
    if log:
        print(f'--- start integrate_mp n_jobs={n_jobs}')
    step = (b - a) / n_jobs
    args = []
    for i in range(n_jobs):
        l = i * step
        r = (i + 1) * step
        args.append(Arg(f, l, r, (n_iter + n_jobs - 1) // n_jobs, log))

    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        res = sum(executor.map(integrate, args))

    end = time.time()
    if log:
        print(f'--- end integrate_mp n_jobs={n_jobs}')
    if log_exp:
        log_exp.write(f'integrate_mp n_jobs={n_jobs} time={end - start}, res={res}\n')
    return res


def experiment():
    with open("artifacts/medium_exp.txt", 'w') as log_exp:
        for i in range(1, 9):
            print(integrate_mp(math.cos, 0, math.pi / 2, n_jobs=i, log=True, log_exp=log_exp))


if __name__ == '__main__':
    experiment()
