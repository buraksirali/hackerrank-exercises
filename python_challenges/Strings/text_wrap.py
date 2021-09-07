# Pypy 3 Solution

def wrap(string, max_width):
    index = 0
    result = ""
    while index < len(string):
        result += string[index: index + max_width]
        result += "\n"
        index += max_width
    string[index: len(string)]
        
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)