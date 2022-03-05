import codecs
from datetime import datetime
from multiprocessing import Queue, Process
from time import sleep


def worker_a(main_to_a: Queue, a_to_b: Queue):
    while True:
        a_to_b.put(main_to_a.get().lower())
        sleep(5)


def worker_b(a_to_b: Queue, b_to_main: Queue):
    while True:
        b_to_main.put(codecs.encode(a_to_b.get(), 'rot_13'))


def main():
    main_to_a = Queue()
    a_to_b = Queue()
    b_to_main = Queue()
    Process(target=worker_a, args=(main_to_a, a_to_b), daemon=True).start()
    Process(target=worker_b, args=(a_to_b, b_to_main), daemon=True).start()
    while True:
        while not b_to_main.empty():
            print(datetime.now().strftime("%H:%M:%S") + " --> " + b_to_main.get())
        main_to_a.put(input(datetime.now().strftime("%H:%M:%S") + " <-- "))


if __name__ == '__main__':
    main()
