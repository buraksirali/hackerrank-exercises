# Python 3 Solution

set_length = int(input())
set_input = set(map(int, input().split()))

instruction_count = int(input())

for _ in range(instruction_count):
    instruction = input().split()
    try:
        if instruction[0] == "pop":
            set_input.pop()
        elif instruction[0] == "discard":
            set_input.discard(int(instruction[1]))
        elif instruction[0] == "remove":
            set_input.remove(int(instruction[1]))
    except KeyError:
        continue
        
print(sum(set_input))