#!/usr/bin/python3

def parse_input(path:str) -> tuple[list[str], tuple[int, int]]:
    """
    Splits the lines of the input file and
    return the starting position coordinates
    """
    with open(path) as file:
        diagram = file.read().splitlines()

    for line in range(len(diagram)):
        if 'S' in diagram[line]:
            start = (diagram[line].index('S'), line)
            break

    return start, diagram

def farthest_tile(start:tuple[int, int], diagram:tuple[list[str]]) -> int:
    pipes = {
            '|': [(0, -1), (0, 1)], '-': [(-1, 0), (1, 0)],
            'L': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)],
            '7': [(0, 1), (-1, 0)], 'F': [(0, 1), (1, 0)],
            # 'S': [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
            }
    paths = [[start], [start]]

    for pipe in pipes.keys():
        chars = []
        for coords in pipes[pipe]:
            coords = (start[0]+coords[0], start[1]+coords[1])
            if coords[0] >= 0 and coords[1] >= 0:
                if diagram[coords[1]][coords[0]] == '.':
                    chars.append('.')
                else:
                    chars.append((coords[0], coords[1]))
            else:
                chars.append('.')

        valid = []
        if '.' not in chars:
            valid = []
            for char in chars:
                look = pipes[diagram[char[1]][char[0]]]
                if (char[0]+look[0][0], char[1]+look[0][1]) == start or (char[0]+look[1][0], char[1]+look[1][1]) == start:
                    valid.append(True)

        if False not in valid and len(valid) == 2:
            diagram[start[1]] = diagram[start[1]].replace('S', pipe)
            paths[0].append((start[0]+pipes[pipe][0][0], start[1]+pipes[pipe][0][1]))
            paths[1].append((start[0]+pipes[pipe][1][0], start[1]+pipes[pipe][1][1]))
            break

    while paths[0][-1] != paths[1][-1]:
        for path in range(len(paths)):
            current = paths[path][-1]
            look = pipes[diagram[current[1]][current[0]]].copy()
            for pos in range(len(look)):
                look[pos] = (look[pos][0]+current[0], look[pos][1]+current[1])
            for pos in look:
                if pos not in paths[path]:
                    paths[path].append(pos)
                    break

    return len(paths[0])-1


if __name__ == '__main__':
    start, diagram = parse_input('input')

    # Part 1
    farthest = farthest_tile(start, diagram)
    print(f"The farthest point in the pipe is {farthest} steps from the starting posisition")
