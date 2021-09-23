# Pypy 3 Solution

_ = input()

set_1 = set(map(int, input().split()))

_ = input()

set_2 = set(map(int, input().split()))

print(len(set_1.symmetric_difference(set_2)))