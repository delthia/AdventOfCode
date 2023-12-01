with open('test-input') as t:
    data = t.read().splitlines()

packets = []
for line in data:
    if line != '':
        packets.append(line[1:-1].split(","))

rights = []
for pair in range(0, len(packets), 2):
    for element in range(0, len(data[pair][1:-1])):
        print(data[pair][element])
        right = False
        try:
            a, b = int(data[pair][element]), int(data[pair+1][element])
        except:
            print('a')
            a, b = None, None
        if type(a) == int and type(b) == int and a < b:
            right = True
    if right:
        rights.append(pair+1)
    print(data[pair])
    print(data[pair+1])

print(right)

# for pair in range(0, len(data), 3):
#     print(data[pair].split(','))
