with open('test-input') as t:
    data = t.read().splitlines()

for command in data:
    if command[0] == '$':
        print('command')
    print(command)
