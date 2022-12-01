#!/usr/bin/python3
data = open("input").read()
fishes = data.split(",")

days = 80   # Amount of days to simulate

for day in range(0, days):
    for fish in range(0, len(fishes)):
        fish = int(fish)
        if int(fishes[fish]) == 0:
            fishes[fish] = 6
            fishes.append(8)
        else:
            fishes[fish] = int(fishes[fish]) - 1

print(len(fishes))
