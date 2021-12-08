import sys
import os

# part 1

gamma = []
epsilon = []

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    length = len(lines[0])-1
    gamma = [0] * length
    epsilon = [0] * length
    j = 0
    for i in range(0, length):
        ones = 0
        for line in lines:
            l = line[0:-1]
            if int(l[j]) == 1:
                ones += 1
        if ones > len(lines) / 2:
            gamma[i] = 1
            epsilon[i] = 0
        else:
            gamma[i] = 0
            epsilon[i] = 1
        j += 1

gamma_res = 0
power = 0
for k in range(len(gamma)-1, -1, -1):
    gamma_res += gamma[k] * 2**power
    power += 1

epsilon_res = 0
power = 0
for k in range(len(epsilon)-1, -1, -1):
    epsilon_res += epsilon[k] * 2**power
    power += 1

print(gamma_res)
print(epsilon_res)

power_consumption = gamma_res * epsilon_res

print(power_consumption)


# part 2
