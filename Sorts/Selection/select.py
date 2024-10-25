from random import randint
from sys import maxsize
from math import floor

directory = "Sorts\\Selection"
worst_file = f"{directory}\\worst_time.txt"
average_file = f"{directory}\\average_time.txt"
best_file = f"{directory}\\best_time.txt"

part_sorted_file = f"{directory}\\part_sorted_time.txt"
title = "Selection_sort"


def selection_sort(nums: list):
    """Изначальная сортировка является нестабильной"""

    n = len(nums)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[i], nums[min_ind] = nums[min_ind], nums[i]

    return nums


def selection_sort_stable(nums: list):
    """Стабильная версия сортировки, но она работает дольше из-за сдвига"""

    n = len(nums)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_ind]:
                min_ind = j

        min_val = nums[min_ind]
        for j in range(min_ind, i, -1):
            nums[j] = nums[j - 1]
        nums[i] = min_val

    return nums


def best_seq(n: int):
    return sorted(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))


def average_seq(n: int):
    return list(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))


def worst_seq(n: int):
    return best_seq(n)[::-1]
