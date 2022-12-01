#!/usr/bin/python3
data = open("input").read().splitlines()

depth = 0
pos = 0
for mod in data:
    print(mod)
    separate = mod.split(' ')
    print(separate)
    if separate[0] == 'up':
        depth -= int(separate[1])
        print('depth ', depth)
    elif separate[0] == 'down':
        depth += int(separate[1])
        print('depth ', depth)
    elif separate[0] == 'forward':
        pos += int(separate[1])
        print('pos ', pos)

print(depth, pos)
print(depth*pos)
