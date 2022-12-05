# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

s = data.index('')
containers = data[:s]
movements = data[s+1:]
c = []
stacks = int((len(data[0])+1)/4)
for x in range(0, stacks):
    c.append([])


for line in containers:
    if '[' not in line:
        break
    else:
        stacks = int((len(line)+1)/4)
        for stack in range(0, stacks):
            container = line[stack*4+1:2+stack*4]
            if container != ' ':
                c[stack].insert(0, container)


for movement in movements:
    move = movement.split(' ')
    for m in range(0, int(move[1])):
        crate = c[int(move[3])-1].pop(-1)
        c[int(move[5])-1].append(crate)


answer = ''
for column in c:
    answer += column[-1]
print(answer)

c = []
stacks = int((len(data[0])+1)/4)
for x in range(0, stacks):
    c.append([])
for line in containers:
    if '[' not in line:
        break
    else:
        stacks = int((len(line)+1)/4)
        for stack in range(0, stacks):
            container = line[stack*4+1:2+stack*4]
            if container != ' ':
                c[stack].insert(0, container)

for movement in movements:
    move = movement.split(' ')
    a = -int(move[1])
    s = int(move[3])-1
    crates = c[s][a:]
    for crate in crates:
        c[int(move[5])-1].append(crate)
    c[s] = c[s][:len(c[s])+a]

answer = ''
for column in c:
    answer += column[-1]
print(answer)
