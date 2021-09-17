# Pypy 3 Solution

import cmath
import math

if __name__ == "__main__":
    z = input()

    neg_present = False
    num = z[1:].split("+")

    if len(num) == 1:
        num = z[1:].split("-")
        neg_present = True

    real_part = int(z[0] + num[0])
    imag_part = int(num[1][:-1])

    if neg_present:
        imag_part = -imag_part
    
    r = math.sqrt(real_part * real_part + imag_part * imag_part)
    phase = cmath.phase(complex(real_part, imag_part))

    print(r)
    print(phase)