# Pypy 3 Solution

from itertools import permutations

if __name__ == "__main__":
    inputs = input().split()
    
    perm_results = list(permutations(inputs[0], int(inputs[1])))
    
    updated_results = []
    for word in perm_results:
        text = ""
        for index in range(int(inputs[1])):
            text += word[index]
            
        updated_results.append(text)
        
    list.sort(updated_results)
    
    for word in updated_results:
        print(word)
