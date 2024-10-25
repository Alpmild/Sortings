from math import floor, log2
from sys import maxsize
from random import randint

directory = "Sorts\\Shell"
title = "Shell_sort"

shell_random_file = f"{directory}\\shell_random_time.txt"
shell_sorted_file = f"{directory}\\shell_sorted_time.txt"
shell_sorted_reverse_file = f"{directory}\\shell_sorted_reverse_time.txt"
shell_part_sorted_file = f"{directory}\\shell_part_sorted_time.txt"

hibbard_random_file = f"{directory}\\hibbard_random_time.txt"
hibbard_sorted_file = f"{directory}\\hibbard_sorted_time.txt"
hibbard_sorted_reverse_file = f"{directory}\\hibbard_sorted_reverse_time.txt"
hibbard_part_sorted_file = f"{directory}\\hibbard_part_sorted_time.txt"

pratt_random_file = f"{directory}\\pratt_random_time.txt"
pratt_sorted_file = f"{directory}\\pratt_sorted_time.txt"
pratt_sorted_reverse_file = f"{directory}\\pratt_sorted_reverse_time.txt"
pratt_part_sorted_file = f"{directory}\\pratt_part_sorted_time.txt"


class Gaps:

    @staticmethod
    def shell(n: int):
        return tuple(map(lambda i: n // (2 ** (i + 1)), range(floor(log2(n)))))

    @staticmethod
    def hibbard(n: int):
        return tuple(map(lambda i: 2 ** i - 1, range(floor(log2(n + 1)), 0, -1)))

    @staticmethod
    def pratt(n: int):
        seq, i = [], 0
        while 2 ** i <= n / 2:
            j = 0
            while 2 ** i * 3 ** j <= n / 2:
                seq.append(2 ** i * 3 ** j)
                j += 1
            i += 1

        return tuple(sorted(seq, reverse=True))


def shell_sort(nums: list, gaps: tuple):
    n = len(nums)

    for gap in gaps:
        for i in range(gap, n, gap):
            x = nums[gap]
            j = i
            while j >= gap and nums[j] < nums[j - gap]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j -= gap
            nums[j] = x

    return nums


def average_seq(n: int):
    return list(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))
