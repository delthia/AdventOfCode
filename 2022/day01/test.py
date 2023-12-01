# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

elf = 0
big = 0
for e in data:
    if e == '':
        if elf > big:
            big = elf
            elf = 0
        else:
            elf = 0
    else:
        elf += int(e)

if int(data[len(data)-1]) > big:
    big = int(data[len(data)-1])

print(big)