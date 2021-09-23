# Pypy 3 Solution

from itertools import product

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = ""
    cartesian = list(product(A,B))
    for prod in cartesian:
        result += str(prod)
        
        if prod != cartesian[-1]: 
            result += " "
            
    print(result)