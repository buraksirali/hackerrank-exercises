# Pypy 3 Solution

import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from Algorithms.quicksort import quick_sort

if __name__ == '__main__':
    len = int(input())
    arr = [int(num) for num in input().split()]

    quick_sort(0, len - 1, arr)

    max = arr.pop()
    runner_up = arr.pop()

    while max == runner_up:
        runner_up = arr.pop()

    print(runner_up)
