# Pypy 3 Solution

def merge_the_tools(string, k):
    for index in range(len(string) // k):
        result = ""
        
        for char in string[index * k:(index + 1) * k]:
            if char not in result:
                result += char
            
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
