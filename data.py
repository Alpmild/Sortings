from time import time
from math import floor
from random import randint
from sys import maxsize, setrecursionlimit
from Sorts.Shell.shell import *

setrecursionlimit(10 ** 9)

cycles = 10
round__ = 5

part_sorted_k = 0.9

file_directory = pratt_sorted_file
list_func = lambda x: sorted_seq(x)
test_sort = lambda seq: shell_sort(seq, Gaps.pratt(len(seq)))

# lengths = (
#     50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000,
#     550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000,
#     1050000, 1100000, 1150000, 1200000,
# )
lengths = (
    2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000,
    18000, 20000, 22000, 24000, 26000, 28000, 30000
)


def random_seq(n: int):
    return list(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))


def sorted_seq(n: int):
    return sorted(random_seq(n))


def sorted_reverse_seq(n: int):
    return sorted(random_seq(n), reverse=True)


def get_lengths(file):
    return tuple(map(int, file.read().split('\n')))


def part_sorted_seq(n: int, k: float):
    n_part = floor(n * k)
    seq = sorted(map(lambda x: randint(-maxsize + 1, maxsize), range(n_part)))
    for i in range(n - n_part):
        seq.insert(randint(0, n + i - 1), randint(-maxsize + 1, maxsize))
    return seq


def get_time(seq: list):
    s = time()
    seq = test_sort(seq)
    f = time()
    seq.clear()
    return f - s


def main():
    try:
        file = open(file_directory, 'a')
    except FileNotFoundError:
        file = open(file_directory, 'w')

    for n in lengths:
        t = 0.0
        for _ in range(cycles):
            res = get_time(list_func(n))
            print(f"{str(n).ljust(12, ' ')} | {round(res, round__)}")
            t += res

        file.write(f"{str(n).ljust(12, ' ')} | {round(t / cycles, round__)}\n")
        print()

    file.close()


if __name__ == "__main__":
    main()
