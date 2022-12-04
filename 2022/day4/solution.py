# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

duplicate = 0
for elf in data:
    elf = elf.split(',')
    group = [elf[0].split('-'), elf[1].split('-')]

    if int(group[0][0])<=int(group[1][0]) and int(group[0][1])>=int(group[1][1]):
        duplicate += 1
    elif int(group[0][0])>=int(group[1][0]) and int(group[0][1])<=int(group[1][1]):
        duplicate += 1

print(duplicate)

overlaps = 0
for elf in data:
    elf = elf.split(',')
    group = [elf[0].split('-'), elf[1].split('-')]

    if int(group[0][0])<=int(group[1][0]) and int(group[0][1])>=int(group[1][1]):
        overlaps += 1
    elif int(group[0][0])>=int(group[1][0]) and int(group[0][1])<=int(group[1][1]):
        overlaps += 1
    elif int(group[0][0])<int(group[1][0]) and int(group[0][1])<int(group[1][1]) and int(group[0][1])>=int(group[1][0]):
        overlaps += 1
    elif int(group[0][0])>int(group[1][0]) and int(group[0][1])>int(group[1][1]) and int(group[0][0])<=int(group[1][1]):
        overlaps += 1

print(overlaps)
