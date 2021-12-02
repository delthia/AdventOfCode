#!/usr/bin/python3
data = open("input").read().splitlines()

larger = 0
for n in range(0, len(data)):
    try:
        value = int(data[n]) + int(data[n+1]) + int(data[n+2])
    except:
        break
    try:
        prev
    except:
        prev = value
    else:
        if int(value) > int(prev):
            larger += 1
    prev = value

print(larger)
