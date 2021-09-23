# Pypy 3 Solution

set_length = int(input())
set_input = set(map(int, input().split()))

instruction_count = int(input())

for _ in range(instruction_count):
    instruction = input().split()
    
    if instruction[0] == "intersection_update":
        set_input.intersection_update(set(map(int, input().split())))
    elif instruction[0] == "update":
        set_input.update(set(map(int, input().split())))
    elif instruction[0] == "symmetric_difference_update":
        set_input.symmetric_difference_update(set(map(int, input().split())))
    elif instruction[0] == "difference_update":
            set_input. difference_update(set(map(int, input().split())))
        
print(sum(set_input))