# Pypy 3 Solution

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    else:
        if 2 <= n < 5:
            print("Not Weird")
        elif n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")