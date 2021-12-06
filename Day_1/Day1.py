import os
import sys

count1 = 0
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    prev = float("inf")
    for line in lines:
        if int(line) > prev:
            count1 += 1
        prev = int(line)

print(count1)


count2 = 0
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    i = 0
    j = 3
    sum = 0
    prev = float("inf")
    for _ in range(len(lines)-2):
        for num in range(i, j):
            sum += int(lines[num])
        if sum > prev:
            count2 += 1
        i += 1
        j += 1
        prev = sum
        sum = 0

print(count2)
