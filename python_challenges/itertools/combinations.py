# Pypy 3 Solution

from itertools import combinations

if __name__ == "__main__":
    inputs = input().split()
    
    final_results = []
    
    for num in range(1, int(inputs[1]) + 1):
        comb_results = list(combinations(inputs[0], num))
        updated_results = []
        
        for word in comb_results:
            text = ""
            for index in range(num):
                text += word[index]
            
            text_list = sorted(text)
            updated_results.append("".join(text_list))
            
        list.sort(updated_results)
        final_results.append(updated_results)
    
    for result in final_results:
        for word in result:
            print(word)