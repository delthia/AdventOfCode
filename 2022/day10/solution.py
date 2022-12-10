# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

x = 1
register_history = []
for cycle in data:
    instruction = cycle.split(' ')
    if instruction[0] == 'noop':
        register_history.append(x)
    elif instruction[0] == 'addx':
        register_history.append(x)
        register_history.append(x)
        x += int(instruction[1])
    else:
        print('The input data contains unknown instructions')
        break

to_check = [20, 40] # Where to start, every how many cycles to check
l = 0
strength = 0
for r in range(0, len(register_history)):
    if l == 0:
        if r+1 == l+to_check[0]:
            strength += (register_history[r]*(r+1))
            l = r+1
    else:
        if r+1 == l+to_check[1]:
            strength += (register_history[r]*(r+1))
            l = r+1

print(strength)
print('-------- Part II --------')

screen = []
size = [40, 6]
# Part two
for line in range(0, size[1]):
    l = ''
    for pixel in range(0, size[0]):
        reg = register_history[pixel+(line*size[0])]
        if reg == pixel or reg+1 == pixel or reg-1 == pixel:
            l += '#'
        else:
            l += '.'
    screen.append(l[:])

for line in screen:
    print(line)
