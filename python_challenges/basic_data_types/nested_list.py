# Pypy 3 Solution

import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from Algorithms.quicksort import quick_sort

if __name__ == '__main__':
    students = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
        scores.append(score)
        
    quick_sort(0, len(scores) - 1, scores)
    lowest = scores.pop(0)
    second_lowest = scores.pop(0)
    while lowest == second_lowest:
        second_lowest = scores.pop(0)

    second_lowest_names = []
    for student in students:
        if student[1] == second_lowest:
            second_lowest_names.append(student[0])

    second_lowest_names.sort()
    for student in second_lowest_names:
        print(student)
