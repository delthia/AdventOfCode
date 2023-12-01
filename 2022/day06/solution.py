# with open('test-input') as t:
with open('input') as t:
    data = t.read()


for character in range(0, len(data)):
    # print(data[character:character+4], '-', set(data[character:character+4]))
    if len(data[character:character+4]) == len(set(data[character:character+4])):
        break

print(character+4)

for character in range(0, len(data)):
    # print(data[character:character+4], '-', set(data[character:character+4]))
    if len(data[character:character+14]) == len(set(data[character:character+14])):
        break

print(character+14)
