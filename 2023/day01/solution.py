#!/usr/bin/python3

if __name__ == '__main__':
    # with open('test-input') as data:
    with open('input') as data:
        lines = data.read().split('\n')

    values = []
    for line in lines:
        first, last = 0, 0
        for character in line:
            if character.isdigit() and first == 0:
                first = int(character)
            elif character.isdigit() and first != 0:
                last = int(character)

        if last == 0:
            last = first
        values.append(first*10+last)

    calibration = sum(values)
    print(f"All the calibration values add up to {calibration}")
