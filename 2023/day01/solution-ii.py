#!/usr/bin/python3

if __name__ == '__main__':
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    with open('test-input-ii') as data:
        lines = data.read().split('\n')

    values = []
    for line in lines:
        first, last = 0, 0
        letterpos = 0
        print(line)
        for digit in digits.keys():
            if digit in line and first == 0:
                print('yes')
                first = digits[digit]
            elif digit in line and first != 0:
                print('yes yes')
                last = digits[digit]
                letterpos = line.index(digit)
        for character in line:
            if character.isdigit() and first == 0:
                first = int(character)
            elif character.isdigit() and first != 0:
                if line.index(character) > letterpos:
                    last = int(character)

        if last == 0:
            last = first
        values.append(first*10+last)

    print(values)
    calibration = sum(values)
    print(f"All the calibration values add up to {calibration}")
