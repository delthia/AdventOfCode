#!/usr/bin/python3
data = open("input").read().splitlines()

commons = [0]*12
for value in data:
    for bit in range(0, len(value)):
        bit = int(bit)
        if value[bit] == '1':
            commons[int(bit)] += 1
for n in range(0, len(commons)):
    if int(commons[n]) > len(data)/2:
        commons[n] = '1'
    elif (commons[n]) < len(data)/2:
        commons[n] = '0'
    else:
        break

print(commons)

primero = data[0]
print(data[0])
print(primero)
for integer in primero:
    print(integer)

clean = data  # Oxygen generator rating candidate list
dirty = data  # CO2 scrubber rating candidate list
for pos in range(0, len(data[0])):
    for byte in data:
        if byte != None:
            if byte[pos] == commons[pos]:
                dirty[pos] = None
            elif byte[pos] != commons[pos] and 1-int(byte[pos]) == commons[pos]:
                clean[por] = None
            else:
                break
        else:
            break

print(clean)
print(dirty)
print(list(filter(None, clean)))
print(list(filter(None, dirty)))
