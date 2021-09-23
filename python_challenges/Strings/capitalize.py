# Pypy 3 Solution

def solve(s):
    result = ""
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            result += word.capitalize()
            word = ""
            result += " "
    
    result += word.capitalize()

    return result

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result + '\n')
