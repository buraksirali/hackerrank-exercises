# Pypy 3 Solution

count = int(input())
values = set()

for _ in range(count):
    values.add(input())
    
print(len(values))