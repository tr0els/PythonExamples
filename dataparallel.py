import time
from concurrent.futures import ProcessPoolExecutor


def print_duration(func, *args):
    start = time.time()
    func(*args)
    finish = time.time()
    print(f'Finished in {round(finish-start, 2)} second(s)')


def cpu_heavy(n):
    count = 0
    for i in range(n + 1):
        count += i
    return count


def sequential(n):
    for i in n:
        cpu_heavy(i)


def parallel(n, workers):
    chunksize = round(len(n) / workers)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        executor.map(cpu_heavy, n, chunksize=chunksize)


if __name__ == '__main__':
    arg = [100] * 1_000_000
    print_duration(sequential, arg)
    print_duration(parallel, arg, 8)
