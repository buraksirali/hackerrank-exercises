# Pypy 3 Solution

size1 = input()
set1 = set(map(int, input().split()))
size2 = input()
set2 = set(map(int, input().split()))

difference = set1.symmetric_difference(set2)
difference_list = [int(num) for num in difference]
difference_list.sort()

for num in difference_list:
    print(num)