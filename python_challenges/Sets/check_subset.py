# Pypy 3 Solution

if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        _ = input()
        set_A = set(map(int, input().split()))

        _ = input()
        set_B = set(map(int, input().split()))

        print(True if set_B.intersection(set_A) == set_A else False)
