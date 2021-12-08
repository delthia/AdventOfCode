#!/usr/bin/python3
data = open("input").read()
fishes = data.split(",")

days = 256   # Amount of days to simulate

"""
for day in range(0, days):
    print(day)
    for fish in range(0, len(fishes)):
        fish = int(fish)
        if int(fishes[fish]) == 0:
            fishes[fish] = 6
            fishes.append(8)
        else:
            fishes[fish] = int(fishes[fish]) - 1

total = len(fishes)
print(total)
"""

# Puede que sea una mejor idea que ir a lo bruto
# https://www.reddit.com/r/adventofcode/comments/radg34/comment/hnhq0bo/?utm_source=share&utm_medium=web2x&context=3

ages = [0]*9
for fish in fishes:
    ages[int(fish)] = int(ages[int(fish)]) + 1

for day in range(0, days):
    born = ages[0]
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7] + born
    ages[7] = ages[8]
    ages[8] = born

print(ages)

total = 0
for age in ages:
    total += int(age)

print(total)
