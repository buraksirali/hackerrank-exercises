# Pypy 3 Solution

def split_and_join(line):
    new_line = line.split()
    result = "-".join(new_line)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)