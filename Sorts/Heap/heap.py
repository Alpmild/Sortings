from random import randint
from sys import maxsize, setrecursionlimit

directory = "Sorts\\Heap"
worst_file = f"{directory}\\worst_time.txt"
average_file = f"{directory}\\average_time.txt"
best_file = f"{directory}\\best_time.txt"

sorted_file = f"{directory}\\sorted_time.txt"
part_sorted_file = f"{directory}\\part_sorted_time.txt"
sorted_reverse_file = f"{directory}\\sorted_reverse_time.txt"
title = "Heap_sort"

setrecursionlimit(10 ** 9)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(nums: list):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return nums


def average_seq(n: int):
    return list(map(lambda x: randint(-maxsize + 1, maxsize), range(n)))
