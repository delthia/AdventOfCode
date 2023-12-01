import re

# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priorities = 0

for backpack in data:
    l = int(len(backpack)/2)
    for letter in backpack[:l]:
        if letter in backpack[l:]:
            break

    priorities += letters.index(letter)+1

print(priorities)

priorities = 0
for index in range(0, len(data)-1, 3):
    for letter in data[index]:
        if letter in data[index+1] and letter in data[index+2]:
            break

    priorities += letters.index(letter)+1

print(priorities)
