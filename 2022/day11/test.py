with open('test-input') as t:
    data = t.read()

def list_of_lists(length):
    list = []
    for x in range(0, length):
        list.append([])
    return list

monkeys = []
for monkey in data.split('\n\n'):
    monkeys.append(monkey.split('\n'))


rounds = 20
inspections = []
for x in range(0, len(monkeys)):
    inspections.append(0)
for r in range(0, rounds):
    print('ROUND ', r)
    mks = list_of_lists(len(monkeys))
    print(monkeys)
    for monkey in monkeys:
        m = monkey[2].split(' ')
        inspections[int(monkey[0].split(' ')[-1].strip(':'))] += len(monkey[1].split(':')[1].split(', '))
        if monkey[1].split(':')[1].split(', ') != ['']:
            for item in monkey[1].split(':')[1].split(', '):
                if m[-1].isdigit() and m[-3] == 'old':
                    if m[-2] == '+':
                        worry = int(item)+int(m[-1])
                    elif m[-2] == '*':
                        worry = int(item)*int(m[-1])
                elif m[-1] == 'old' and m[-3] == 'old':
                    worry = int(item)*int(item)
                # worry = round(worry/3)
                worry = int(str(worry/3).split('.')[0])
                """
                if worry%int(monkey[3].split(' ')[-1]) == 0:
                    if monkeys[int(monkey[4].split(' ')[-1])][1].split(':')[1] == '':
                        monkeys[int(monkey[4].split(' ')[-1])][1] += str(worry)
                    else:
                        monkeys[int(monkey[4].split(' ')[-1])][1] +=', '+str(worry)
                else:
                    if monkeys[int(monkey[5].split(' ')[-1])][1].split(':')[1] == '':
                        monkeys[int(monkey[5].split(' ')[-1])][1] += str(worry)
                    else:
                        monkeys[int(monkey[5].split(' ')[-1])][1] +=', '+str(worry)
                """
                if worry%int(monkey[3].split(' ')[-1]) == 0:
                    mks[int(monkey[4].split(' ')[-1])].append(worry)
                else:
                    mks[int(monkey[5].split(' ')[-1])].append(worry)
                # i += 1
            # inspections[int(monkey[0].split(' ')[-1].strip(':'))] += i
            monkey[1] = monkey[1].split(':')[0]+':'

    for monkey in range(0, len(monkeys)):
        if mks[monkey] != []:
            if monkeys[monkey][1].split(':')[-1] != '':
                monkeys[monkey][1].split(':')[-1] += ', '
            for k in range(0, len(mks[monkey])):
                monkeys[monkey][1] += str(mks[monkey][k])
                if k+1 != len(mks[monkey]):
                    monkeys[monkey][1] += ', '


    """
    for m in range(0, len(mks)):
        print(m)
        if monkeys[int(monkeys[m][2].split(' ')[-1])][1].split(':')[1] != '':
            monkeys[int(monkeys[m][2].splot(' ')[-1])][1] += ', '
        for k in range(0, len(mks[m])):
            monkeys += str(mks[m][k])
            if k+1 != len(mks[m]):
                monkeys += ', '
        """

print(inspections)
