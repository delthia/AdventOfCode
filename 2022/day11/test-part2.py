import sys

# with open('test-input') as t:
with open('input') as t:
    data = t.read()

# sys.set_int_max_str_digits(1000000)

def operation(value, operation):
    if '*' in operation:
        if operation.split(' ')[0] == 'old' and operation.split(' ')[-1] == 'old':
            # result = value*value
            result = value**2
        else:
            result = value*int(operation.split(' ')[-1])
    elif '+' in operation:
        result = value+int(operation.split(' ')[-1])
    return result

def zero_list(length):
    list = []
    for x in range(0, length):
        list.append(0)
    return list

monkeys = []
for monkey in data.split('\n\n'):
    monkeys.append(monkey.split('\n'))

for monkey in monkeys:
    monkey.pop(0)
    monkey[0] = [int(l) for l in (monkey[0].split(':')[-1].split(','))]
    monkey[1] = monkey[1].split('=')[-1][1:]
    monkey[2] = int(monkey[2].split(' ')[-1])
    monkey[3] = int(monkey[3].split(' ')[-1])
    monkey[4] = int(monkey[4].split(' ')[-1])

rounds = 10000
inspections = zero_list(len(monkeys))
for r in range(0, rounds):
    i = 0
    for monkey in monkeys:
        for item in monkey[0]:
            worry = operation(item, monkey[1])
            if worry%monkey[2] == 0:
                monkeys[monkey[3]][0].append(worry)
            else:
                monkeys[monkey[4]][0].append(worry)
        inspections[i] += len(monkey[0])
        monkey[0] = []
        i += 1

inspections.sort()
business = inspections[-1]*inspections[-2]
print(business)
