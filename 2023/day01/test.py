#!/usr/bin/python3

if __name__ == '__main__':
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # with open('test-input-ii') as data:
    with open('input') as data:
        lines = data.read().split('\n')[:-1]    # The last line is empty

    values = [] # Calibration values
    for line in lines:
        thisline = {}   # Temporary storage for digits so I can keep them in order
        
        for digit in digits.keys():
            if digit in line:
                lastindex = 0
                for x in range(line.count(digit)):
                    thisline[line.index(digit, lastindex)] = digits[digit]
                    lastindex = line.index(digit, lastindex)+1
                thisline[line.index(digit)] = digits[digit]

        for pos in range(len(line)):
            if line[pos].isdigit():
                thisline[pos] = line[pos]

        # Translate thisline into a string
        string = ''.join(str(thisline[num]) for num in sorted(thisline.keys()))

        if string != '':
            values.append(int(string[0]+string[-1]))    # Just save the first and last digits

    print(f"All the calibration values add up to {sum(values)}")
