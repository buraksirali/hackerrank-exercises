# Pypy 3 Solution

for num in range(1, int(input())):
    print([1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111][num - 1] * num)