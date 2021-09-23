 # Pypy 3 Solution

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def top_bottom(num,reversed):
    result = ""

    if reversed:
        loop = range(num - 1, -1, -1)
    else:
        loop = range(1, num, 1)
    
    for index in loop:
        symbole = '-' * index * 2

        row = ""
        row += symbole

        for sec_index in range(num - index):
            row += alphabet[num - sec_index - 1]

            if sec_index != num - index - 1:
                row += '-'

        row += reverse_text(row[:len(row) - 1])
        
        if reversed or (not reversed and index != num - 1):
            row += '\n'
        
        result += row

    return result

    
def reverse_text(text):
    result = []

    for char in text:
        result.insert(0, char)

    return ''.join(result)


def print_rangoli(n):
    length = n
    print(top_bottom(length, True) + top_bottom(length, False))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
