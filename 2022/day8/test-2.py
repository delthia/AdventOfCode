with open('test-input') as t:
    data = t.read().splitlines()

visible = len(data[0])*4-4

for row in range(1, len(data[0])-1):
    for column in range(1, len(data[row])-1):
        tree = int(data[row][column])
        l,r,u,d = True,True,True,True
        for x in range(column+1, len(data[row])):
            if int(data[row][x]) >= tree:
                r = False
                break
        for x in range(column-1, -1, -1):
            if int(data[row][x]) >= tree:
                l = False
                break
        for x in range(column+2, len(data[row])):
            if int(data[x][column]) >= tree:
                d = False
                break
        for x in range(column, -1, -1):
            if int(data[x][column]) >= tree:
                u = False
                break

        if l or r or u or d:
            print(tree)
            print('Visible')
            visible += 1

        if l:
            print('l')
        if r:
            print('r')
        if d:
            print('d')
        if u:
            print('u')

print(visible)
