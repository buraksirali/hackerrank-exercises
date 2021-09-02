# Pypy 3 Solution

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    tuple_of_list = tuple(integer_list)
    print(hash(tuple_of_list))