#!/usr/bin/python3
data = open("input").read()
fishes = data.split(",")

days = 256   # Amount of days to simulate

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

total = 0
for age in ages:
    total += int(age)

print(total)
