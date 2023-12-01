# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

row = 3
column = 3

visible = len(data[0])*4-4

for row in range(1, len(data[0])-1):
    for column in range(1, len(data[row])-1):
        tree = int(data[row][column])
        l, r, d, u = True, True, True, True
        for x in range(column+1, len(data[row])):
            if int(data[row][x]) >= tree:
                l = False
                break
        for x in range(column-1, -1, -1):
            if int(data[row][x]) >= tree:
                r = False
                break
        for x in range(row+1, len(data)):
            if int(data[x][column]) >= tree:
                d = False
                break
        for x in range(row-1, -1, -1):
            if int(data[x][column]) >= tree:
                u = False
                break

        if l or r or d or u:
            visible += 1

print(visible)

best = 0
for row in range(1, len(data[0])-1):
    for column in range(1, len(data[row])-1):
        tree = int(data[row][column])
        score = 1
        
        y = 0
        for x in range(column+1, len(data[row])):
            y += 1
            if int(data[row][x]) >= tree:
                break
        score *= y

        y = 0
        for x in range(column-1, -1, -1):
            y += 1
            if int(data[row][x]) >= tree:
                break
        score *= y

        y = 0
        for x in range(row+1, len(data)):
            y += 1
            if int(data[x][column]) >= tree:
                break
        score *= y

        y = 0
        for x in range(row-1, -1, -1):
            y += 1
            if int(data[x][column]) >= tree:
                break
        score *= y

        if score > best:
            best = score

print(best)
