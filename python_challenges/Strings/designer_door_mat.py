# Pypy 3 Solution

def top_bottom(height, reversed):
    result = ''
    symboles = ['-', '.|.']

    if reversed:
        looper = range(height - 1, -1, -1)
    else:
        looper = range(height)

    for num in looper:
        first_symbole = symboles[0] * ((height - num) * 3)
        second_symbole = symboles[1] * (1 + num * 2)

        result += first_symbole + second_symbole + first_symbole

        if (reversed and num != 0) or (not reversed and num != (height - 1)):
            result += '\n'
    
    return result


def middle(width):
    symbole = '-' * width
    return '\n' + symbole + 'WELCOME' + symbole + '\n'


if __name__ == "__main__":
    s = input()
    inputs = s.split()
    height = int(inputs[0]) // 2
    width = (int(inputs[1]) - 7) // 2

    print(top_bottom(height, False) + middle(width) + top_bottom(height, True))

