from random import randint
from sys import maxsize
from math import floor

directory = "Sorts\\Insertion"
worst_file = f"{directory}\\worst_time.txt"
average_file = f"{directory}\\average_time.txt"
best_file = f"{directory}\\best_time.txt"

part_sorted_file = f"{directory}\\part_sorted_time.txt"
title = "Insertion_sort"


def insertion_sort(nums: list):
    """Сортировка является устойчивой из-за сдвига"""

    n = len(nums)
    for i in range(1, n):
        x, j = nums[i], i

        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
        nums[j] = x

    return nums


def best_seq(n: int):
    return sorted(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))


def average_seq(n: int):
    return list(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))


def worst_seq(n: int):
    return best_seq(n)[::-1]

