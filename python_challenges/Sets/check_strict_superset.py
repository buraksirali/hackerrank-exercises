# Pypy 3 Solution

def is_super_set(set_A, set_count):
    for _ in range(set_count):
        set_x = set(map(int, input().split()))
        
        if set_A.intersection(set_x) == set_x and len(set_A) > len(set_x):
            continue
        else:
            return False
    
    return True


if __name__ == "__main__":
    set_A = set(map(int, input().split()))
    set_count = int(input())
    
    print(is_super_set(set_A, set_count))
    