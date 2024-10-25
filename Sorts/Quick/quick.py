from random import randint
from sys import maxsize, setrecursionlimit
from math import floor, ceil

directory = "Sorts\\Quick"
worst_file = f"{directory}\\worst_time.txt"
average_file = f"{directory}\\average_time.txt"
best_file = f"{directory}\\best_time.txt"

sorted_file = f"{directory}\\sorted_time.txt"
part_sorted_file = f"{directory}\\part_sorted_time.txt"
random_file = f"{directory}\\random_time.txt"
title = "Quick_sort"

average_k = 0.75
best_k = 0.5

setrecursionlimit(10 ** 9)


def quick_sort(a):
    n, ind, i = len(a), 0, 0
    la, ra = [], []

    if n <= 1:
        return a
    while i < n:
        if i != ind:
            if a[i] < a[ind]:
                la.append(a[i])
            else:
                ra.append(a[i])
        i += 1

    return quick_sort(la) + [a[ind]] + quick_sort(ra)


def quick_sort_stable(a):
    """Сортировка является устойчивой"""

    n, ind, i = len(a), 0, 0
    la, ma, ra = [], [], []
    if a:
        ma = [a[ind]]

    if n <= 1:
        return a
    while i < n:
        if i != ind:
            if a[i] < a[ind]:
                la.append(a[i])
            elif a[i] > a[ind]:
                ra.append(a[i])
            else:
                ma.append(a[i])
        i += 1

    return quick_sort(la) + ma + quick_sort(ra)


def divided_seq(n: int, k: float, down_bord=-maxsize + 1, up_bord=maxsize):
    a = randint(down_bord, up_bord)
    if n == 0:
        return []
    return [a, *divided_seq(floor((n - 1) * k), k, down_bord, a),
            *divided_seq(ceil((n - 1) * (1 - k)), k,  a, up_bord)]


def best_seq(n: int):
    return divided_seq(n, best_k)


def average_seq(n: int):
    return divided_seq(n, average_k)


def worst_seq(n: int):
    return sorted(map(lambda x: randint(-maxsize + 1, maxsize), range(n)), reverse=True)
