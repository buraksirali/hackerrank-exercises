# Pypy 3 Solution

def top_chars(char, num):
    for index in range(1, num + 1):
        symbol = char * (index * 2 - 1)
        print(symbol.rjust(num * 2 - (num - index) - 1))


def bottom_chars(char, num):
    for index in range(num, 0, -1):
        symbol = char * (index * 2 - 1)
        result = f"{symbol}".rjust(num * 6 - (num - index + 1))
        print(result)


def letter(char, num):
    top_bottom_letter(char, num)
    mid_letter(char, num)
    top_bottom_letter(char, num)


def top_bottom_letter(char, num):
    symbol = char * num
    
    for _ in range(num + 1):
        result = "".rjust(num // 2)
        result += symbol + symbol.rjust(num * 4)
        print(result)


def mid_letter(char, num):
    for _ in range(num // 2 + 1):
        result = "".rjust(num // 2)
        result += char * (num * 5)
        print(result)


if __name__ == '__main__':
    thickness = int(input())
    char = "H"
    top_chars(char, thickness)
    letter(char, thickness)
    bottom_chars(char, thickness)