# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

data.append('')
elf = 0
big = [0, 0, 0]
for e in data:
    print(e)
    if e == '':
        print(elf)
        if elf > big[0]:
            big[2] = big[1]
            big[1] = big[0]
            big[0] = elf
        elif elf > big[1]:
            big[2] = big[1]
            big[1] = elf
        elif elf > big[2]:
            big[2] = elf
        elf = 0
    else:
        elf += int(e)


print(big)
print('The elf that carries the most calories carries:', big[0])
print('The three elves that carry the most calories, toghether carry:', big[0]+big[1]+big[2])