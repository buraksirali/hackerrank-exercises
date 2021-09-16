# Pypy 3 Solution

import sys, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from Algorithms.boyer_moore_horspool import boyer_moore_horspool

if __name__ == "__main__":
    print(len(boyer_moore_horspool("cdc", "cdcdcdc")))