#!/usr/bin/python3
data = open("input").read().splitlines()

depth = 0
pos = 0
for mod in data:
    separate = mod.split(' ')
    if separate[0] == 'up':
        depth -= int(separate[1])
    elif separate[0] == 'down':
        depth += int(separate[1])
    elif separate[0] == 'forward':
        pos += int(separate[1])

print(depth*pos)
