# Pypy 3 Solution

if __name__ == "__main__":
    group_size = int(input())
    room_numbers = list(map(int, input().split()))
    
    unique_room_nums = set(room_numbers)
    
    num_counts = {}
    for num in unique_room_nums:
        num_counts[num] = 0
        
    for num in room_numbers:
        if num in unique_room_nums:
            num_counts[num] += 1
            
            if num_counts[num] == 2:
                unique_room_nums.discard(num)
    print(unique_room_nums.pop())