# Pypy 3 Solution

def average(array):
    array_set = set(array)
    
    return sum(array_set) / len(array_set)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)