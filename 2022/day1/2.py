# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

elf = 0
big = [0, 0, 0]
for e in data:
    if e == '':
        if elf > big[0]:
            big[2] = big[1]
            big[1] = big[0]
            big[0] = elf
            elf = 0
            print('1')
        elif elf > big[1]:
            big[1] = big[0]
            big[1] = elf
            elf = 0
            print('2')
        elif elf > big[2]:
            big[2] = elf
            elf = 0
            print('3')
        else:
            elf = 0
        print(big)
    else:
        elf += int(e)

print(int(data[len(data)-1]))
if int(data[len(data)-1]) > big[0]:
    big[2] = big[1]
    big[1] = big[0]
    big[0] = int(data[len(data)-1])
    elf = 0
elif int(data[len(data)-1]) > big[1]:
    big[1] = big[0]
    big[1] = int(data[len(data)-1])
    elf = 0
elif int(data[len(data)-1]) > big[2]:
    big[2] = int(data[len(data)-1])
    elf = 0

print(big)
print(big[0]+big[1]+big[2])