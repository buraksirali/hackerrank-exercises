# Pypy 3 Solution

import math

result = round(math.atan(int(input()) / int(input())) / math.pi * 180)
print(f"{result}" + u"\N{DEGREE SIGN}")