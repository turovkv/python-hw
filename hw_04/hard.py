import codecs
from datetime import datetime
from multiprocessing import Queue, Process
from threading import Thread
from time import sleep


def worker_a(main_to_a: Queue, a_to_b: Queue):
    while True:
        a_to_b.put(main_to_a.get().lower())
        sleep(5)


def worker_b(a_to_b: Queue, b_to_main: Queue):
    while True:
        b_to_main.put(codecs.encode(a_to_b.get(), 'rot_13'))


def main_in(main_to_a):
    while True:
        val = input()
        main_to_a.put(val)
        print(datetime.now().strftime("%H:%M:%S") + " <-- " + val)


def main_out(b_to_main):
    while True:
        print(datetime.now().strftime("%H:%M:%S") + " --> " + b_to_main.get())


def main():
    main_to_a = Queue()
    a_to_b = Queue()
    b_to_main = Queue()
    Process(target=worker_a, args=(main_to_a, a_to_b), daemon=True).start()
    Process(target=worker_b, args=(a_to_b, b_to_main), daemon=True).start()
    Thread(target=main_in, args=(main_to_a,), daemon=True).start()
    Thread(target=main_out, args=(b_to_main,)).start()


if __name__ == '__main__':
    main()
