import time
from multiprocessing import Process


def print_duration(func, *args):
    start = time.time()
    func(*args)
    finish = time.time()
    print(f'Finished in {round(finish-start, 2)} second(s)')


def brew_coffee():
    time.sleep(4)


def make_toast():
    time.sleep(2)


def fry_eggs():
    time.sleep(3)


def parallel():
    processes = [Process(target=brew_coffee),
                 Process(target=make_toast),
                 Process(target=fry_eggs)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


def sequential():
    brew_coffee()
    make_toast()
    fry_eggs()


if __name__ == '__main__':
    print_duration(sequential)
    print_duration(parallel)
