# Pypy 3 Solution

if __name__ == "__main__":
    first = int(input())
    second = int(input())
    
    result = divmod(first, second)
    
    print(f"{result[0]}\n{result[1]}\n{result}")