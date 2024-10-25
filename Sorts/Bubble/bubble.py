from random import randint
from sys import maxsize

title = "Bubble_sort"

directory = "Sorts\\Bubble"
worst_file = f"{directory}\\worst_time.txt"
average_file = f"{directory}\\average_time.txt"
best_file = f"{directory}\\best_time.txt"

part_sorted_file = f"{directory}\\part_sorted_time.txt"


def bubble_sort(nums: list):
    """Сортировка является стабильной"""

    n = len(nums)
    t = True

    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                t = False
        if t:
            break

    return nums


def best_seq(n: int):
    return sorted(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))


def average_seq(n: int):
    n_2 = n // 2
    seq = best_seq(n_2)
    for i in range(n - n_2):
        seq.insert(randint(0, n + i - 1), randint(-maxsize + 1, maxsize))


def worst_seq(n: int):
    return best_seq(n)[::-1]
