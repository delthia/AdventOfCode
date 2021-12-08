#!/usr/bin/python3
data = open("input").read()
fishes = data.split(",")

days = 256   # Amount of days to simulate

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
