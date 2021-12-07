#!/usr/bin/python3
data = open("input").read().splitlines()

commons = [0]*12
for value in data:
    for bit in range(0, len(value)):
        bit = int(bit)
        if value[bit] == '1':
            commons[int(bit)] += 1

gamma = [0]*12
epsilon = [0]*12
for n in range(0, len(commons)):
    if int(commons[n]) > len(data)/2:
        gamma[n] = '1'
        epsilon[n] = '0'
    elif (commons[n]) < len(data)/2:
        gamma[n] = '0'
        epsilon[n] = '1'
    else:
        break

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print(gamma*epsilon)
