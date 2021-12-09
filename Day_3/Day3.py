import sys
import os

# part 1

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
        if ones >= len(lines) / 2:
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
print(gamma_res * epsilon_res)


# part 2

def find_gamma(lst):
    lines = lst
    length = len(lines[0])
    gamma = [0] * length
    j = 0
    for i in range(0, length):
        ones = 0
        for line in lines:
            if int(line[j]) == 1:
                ones += 1
        if ones >= len(lines) / 2:
            gamma[i] = 1
        else:
            gamma[i] = 0
        j += 1
    return gamma


def find_epsilon(lst):
    lines = lst
    length = len(lines[0])
    epsilon = [0] * length
    j = 0
    for i in range(0, length):
        ones = 0
        for line in lines:
            if int(line[j]) == 1:
                ones += 1
        if ones >= len(lines) / 2:
            epsilon[i] = 0
        else:
            epsilon[i] = 1
        j += 1
    return epsilon


with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    length = len(lines[0])-1
    oxygen = []
    co2 = []
    for line in lines:
        oxygen.append(line[0:-1])
        co2.append(line[0:-1])

gamma = find_gamma(oxygen)
i = 0
while i < 12:
    for j in range(len(oxygen)-1, -1, -1):
        if int(oxygen[j][i]) != gamma[i] and len(oxygen) > 1:
            oxygen.pop(j)
        elif len(oxygen) == 1:
            break
    gamma = find_gamma(oxygen)
    i += 1

epsilon = find_epsilon(co2)
k = 0
while k < 12:
    for l in range(len(co2)-1, -1, -1):
        if int(co2[l][k]) != epsilon[k] and len(co2) > 1:
            co2.pop(l)
        elif len(co2) == 1:
            break
    epsilon = find_epsilon(co2)
    k += 1

oxygen_res = 0
power = 0
for i in range(len(gamma)-1, -1, -1):
    oxygen_res += int(oxygen[0][i]) * 2**power
    power += 1

co2_res = 0
power = 0
for j in range(len(epsilon)-1, -1, -1):
    co2_res += int(co2[0][j]) * 2**power
    power += 1

print(oxygen_res)
print(co2_res)
print(oxygen_res * co2_res)
