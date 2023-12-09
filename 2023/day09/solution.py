#!/usr/bin/python3

def parse_input(path:str) -> list[list]:
    with open(path) as file:
        data = file.read().splitlines()

    histories = [list(map(lambda x: int(x), history.split())) for history in data]
    
    return histories


def step_differences(histories:list) -> list[list[list]]:
    differences, lines = [[history] for history in histories], [history for history in histories]
    for line in range(len(lines)):
        while len(set(lines[line])) != 1 or list(set(lines[line]))[0] != 0:
            newline = []
            for pos in range(1, len(lines[line])):
                newline.append(lines[line][pos]-lines[line][pos-1])
            lines[line] = newline
            differences[line].append(lines[line])

    return differences


def extrapolate_history(histories:str) -> list:
    extrapolated = []
    for history in histories:
        value = 0
        for x in range(len(history)-2, -1, -1):
            value += history[x][-1]
        extrapolated.append(value)

    return extrapolated


if __name__ == '__main__':
    histories = parse_input('input')
    differences = step_differences(histories)

    # Part 1
    extrapolated = extrapolate_history(differences)
    print(f"All the extrapolated values add up to {sum(extrapolated)}")
