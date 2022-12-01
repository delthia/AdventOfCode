#!/usr/bin/python3
data = open("input").read().splitlines()
#data = open("data-2").read().splitlines()

larger = 0
for value in data:
    try:
        prev
    except:
        print("Prev no existe")
    else:
        if int(value) > int(prev):
            # print(value, '>', prev)
            print(value, '(increased)')
            larger += 1
            print(larger)
        # elif value < prev:
        # else:
            # print(value, '<', prev)
            # print(value, '(decreased)')
    prev = value
    # print(larger)

print(larger)

# Hay que trabajar con integers
# https://www.reddit.com/r/adventofcode/comments/r6gmpc/2021_day_1_not_sure_what_is_tripping_me_up/
