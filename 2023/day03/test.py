#!/usr/bin/python3
def parse_input(data:list) -> tuple:
    coords = [] # Store where a number starts and its length
    symbols = []    # Store where symbols that are not dots are
    for line in range(len(data)):
        number = False
        for symbol in range(len(data[line])):
            if data[line][symbol].isdigit():
                if number == False:
                    number = True
                    coords.append([[symbol, line], 1])
                else:
                    # If the next character is also a digit, add to the length
                    coords[-1][-1] += 1
            else:
                number = False
                if data[line][symbol] != '.':
                    symbols.append([symbol, line])

    return coords, symbols

def part1(path:str) -> None:
    with open(path) as file:
        data = file.read().splitlines()

    coords, symbols = parse_input(data)

    numbers = []    # All the valid numbers
    for symbol in coords:
        start = symbol[0][0]
        end = symbol[0][0] + symbol[1]-1
        line = symbol[0][1]
        changes = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1]]
        for change in changes:
            if [start+change[0], line+change[1]] in symbols or [end+change[0], line+change[1]] in symbols:
                numbers.append(symbol)
                break

    addition = 0    # Add them toghether
    for number in numbers:
        addition += int(data[number[0][1]][number[0][0]:number[0][0]+number[1]])

    print(f"All the valid numbers add up to {addition}")

def part2(path:str) -> None:
    with open(path) as file:
        data = file.read().splitlines()

    ratios = 0
    for line in range(len(data)):
        for symbol in range(len(data[line])):
            if data[line][symbol] == '*':
                gears = []
                valid = [[symbol-1, line-1], [symbol, line-1], [symbol+1, line-1], [symbol-1, line], [symbol+1, line], [symbol-1, line+1], [symbol, line+1], [symbol+1, line+1]]
                coords, symbols = parse_input(data[line-1:line+2])
                # Adjust lines to make them match with the full input data
                for elem in range(len(coords)):
                    coords[elem][0][1] += line-1
                for num in coords:
                    for coord in range(num[1]):
                        if [num[0][0]+coord, num[0][1]] in valid:
                            gears.append(int(data[num[0][1]][num[0][0]:num[0][0]+num[1]]))
                            break
                if len(gears) == 2:
                    ratios += gears[0]*gears[1]

    print(f"All the ratios add up to {ratios}")


if __name__ == '__main__':
    # load_data('test-input')
    part1('input')

    # part2('test-input')
    part2('input')
