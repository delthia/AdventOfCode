#!/usr/bin/python3
data = open("input").read().splitlines()

commons = [0]*12
inverted = [0]*12
for value in data:
    for bit in range(0, len(value)):
        bit = int(bit)
        if value[bit] == '0':
            print('A zero')
            inverted[int(bit)] += 1
        elif value[bit] == '1':
            print('A one')
            commons[int(bit)] += 1
        print(bit)
    print('End of byte')

print(len(data), ' bytes')
print(commons)
print(inverted)

gamma = [0]*12
epsilon = [0]*12
for n in range(0, len(commons)):
    if int(commons[n]) > (inverted[n]):
        print('1 is more common than 0')
        gamma[n] = '1'
        epsilon[n] = '0'
    elif (commons[n]) < (inverted[n]):
        print('0 is more common than 1')
        gamma[n] = '0'
        epsilon[n] = '1'
    else:
        print('something whent wrong, there was a value out of the expected range')


gamma = ''.join(gamma)
epsilon = ''.join(epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma)
print(epsilon)
print('Power:', gamma*epsilon)

# Se puede convertir una cadena de binario en un decimal utilizando int(cadena, 2)
