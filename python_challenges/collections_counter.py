# Pypy 3 Solution

num_of_shoes = int(input())
shoe_types = input().split()
num_of_purchases = int(input())
sum = 0

for index in range(num_of_purchases):
    purchase = input().split()
    if purchase[0] in shoe_types:
        shoe_types.remove(purchase[0])
        sum += int(purchase[1])

print(sum) 
