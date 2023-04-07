#!/usr/bin/env python
rows = int(input("Enter rows: "))

# the outer loop is executing
# in reversed order
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end='')
    print(" ")
