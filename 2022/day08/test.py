with open('test-input') as t:
    data = t.read().splitlines()

def is_visible(direccion, sentido, posicion):
    print('a')
    small = 0
    y = 0
    if sentido == 1:
        for x in range(posicion, len(direccion)):
            tree = x+1
            y += 1
            if int(direccion[posicion]) > int(direccion[tree])
                small += 1
        if small = y:
            return True
    elif sentido == -1:
        for x in range(posicion, 0, -1):
            tree = x-1
            y += 1
            if int(direccion[posicion]) > int(direccion[tree])
                small += 1
        if small = y:
            return True
    else:
        pass


visible = len(data[0])*4-4
for row in range(1, len(data[0])-1):
    print(data[row])
    for column in range(1, len(data[row])-1):
        tree = int(data[row][column])
        print(tree)
        # if tree > int(data[row-1][column]) or tree > int(data[row+1][column]) or tree > int(data[row][column-1]) or tree > int(data[row][column+1]):
        if is_visible(x, 1, x) or is_visible(x, -1, column) or is_visible(x, 1, column) or is_visible(x, -1, column):
            print('Visible')
            visible += 1

print(visible)

is_visible(data[0], -1, 5)
is_visible(data[0], 1, 3)
