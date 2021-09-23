# Pypy 3 Solution

from itertools import combinations_with_replacement

if __name__ == "__main__":
    inputs = list(input().split())
    
    combs = list(combinations_with_replacement(inputs[0], int(inputs[1])))
    
    result = []
    for comb in combs:
        word = ""
        
        for num in range(int(inputs[1])):
            word += comb[num]
        
        word_sorted = sorted(word)
        word = "".join(word_sorted)
        
        result.append(word)
            
    list.sort(result)
    
    for word in result:
        print(word)