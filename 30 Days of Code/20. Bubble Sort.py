#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

no_of_swaps = 0
for i in range(len(a)):
    swaps = 0
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
            no_of_swaps += 1
    if swaps == 0:
        break
print(f"Array is sorted in {no_of_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")