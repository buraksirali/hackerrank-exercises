# Pypy 3 Solution

if __name__ == "__main__":
    _ = input()
    array = list(map(int, input().split()))
    
    set_happiness = set(map(int, input().split()))
    set_sadness = set(map(int, input().split()))
    
    dict_points = {}
    
    for num in set_happiness:
        dict_points[num] = 1
        
    for num in set_sadness:
        dict_points[num] = -1
        
    mental_state = 0
    
    for num in array:
        if num in dict_points.keys():
            mental_state += dict_points[num]
            
    print(mental_state)