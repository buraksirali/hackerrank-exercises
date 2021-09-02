from quicksort import quick_sort

len = int(input())
arr = [int(num) for num in input().split()]

quick_sort(0, len - 1, arr)

max = arr.pop()
runner_up = arr.pop()

while max == runner_up:
    runner_up = arr.pop()

print(runner_up)
