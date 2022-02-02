def get_fib_list(n: int):
    fib_list = [1, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


if __name__ == "__main__":
    print(get_fib_list(int(input())))
