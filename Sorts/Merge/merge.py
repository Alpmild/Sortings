from random import randint
from sys import maxsize, setrecursionlimit
from math import ceil, floor

directory = "Sorts\\Merge"
worst_file = f"{directory}\\worst_time.txt"
average_file = f"{directory}\\average_time.txt"
best_file = f"{directory}\\best_time.txt"

sorted_file = f"{directory}\\sorted_time.txt"
part_sorted_file = f"{directory}\\part_sorted_time.txt"
sorted_reverse_file = f"{directory}\\sorted_reverse_time.txt"
title = "Merge_sort"

setrecursionlimit(10 ** 9)


def merge(a: list, b: list):
    k, m = len(a), len(b)
    i, j = 0, 0
    c = []

    while i < k and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i == k:
        while j < m:
            c.append(b[j])
            j += 1
    else:
        while i < k:
            c.append(a[i])
            i += 1

    return c


def merge_sort(a: list):
    n = len(a)
    if n == 1:
        return a.copy()
    else:
        return merge(merge_sort(a[:n // 2]), merge_sort(a[n // 2:]))


def average_seq(n: int):
    return list(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))
