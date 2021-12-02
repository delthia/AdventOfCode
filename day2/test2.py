#!/usr/bin/python3
data = open("input").read().splitlines()

depth = 0
pos = 0
aim = 0
for mod in data:
    print(mod)
    separate = mod.split(' ')
    print(separate)
    if separate[0] == 'up':
        aim -= int(separate[1])
        print('aim ', aim)
    elif separate[0] == 'down':
        aim += int(separate[1])
        print('aim ', aim)
    elif separate[0] == 'forward':
        pos += int(separate[1])
        depth += int(aim)*int(separate[1])
        print('pos ', pos)
        print('aim ', aim)

print(depth, pos)
print(depth*pos)
