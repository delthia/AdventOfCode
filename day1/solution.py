#!/usr/bin/python3
data = open("input").read().splitlines()

larger = 0
for value in data:
    try:
        prev
    except:
        prev = value
    else:
        if int(value) > int(prev):
            larger += 1
    prev = value

print(larger)
