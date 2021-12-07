import os
import sys


# part 1

class Submarine:
    depth = 0
    horizontal = 0


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    for line in lines:
        instruction = line.strip().split()
        if instruction[0] == "forward":
            Submarine.horizontal += int(instruction[1])
        elif instruction[0] == "up":
            Submarine.depth -= int(instruction[1])
        elif instruction[0] == "down":
            Submarine.depth += int(instruction[1])

result = Submarine.depth * Submarine.horizontal

print(result)


# part 2

class Submarine:
    depth = 0
    horizontal = 0
    aim = 0


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    for line in lines:
        instruction = line.strip().split()
        if instruction[0] == "forward":
            Submarine.horizontal += int(instruction[1])
            Submarine.depth += Submarine.aim * int(instruction[1])
        elif instruction[0] == "up":
            Submarine.aim -= int(instruction[1])
        elif instruction[0] == "down":
            Submarine.aim += int(instruction[1])

result = Submarine.depth * Submarine.horizontal

print(result)
