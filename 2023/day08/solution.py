#!/usr/bin/python3
import math

def parse_input(path:str) -> tuple[str, dict[int, tuple[int, int]]]:
    with open(path) as file:
        data = file.read().splitlines()

    instructions = data[0]

    nodes = {}
    for node in data[2:]:
        cut = node.split(' = ')
        node_id = cut[0]
        connections = (cut[1].split(', ')[0][1:], cut[1].split(', ')[1][:-1])
        nodes[node_id] = connections

    return instructions, nodes

def count_steps(instructions:str, nodes:dict[int, tuple[int, int]]) -> int:
    steps, pos, dirs = 0, 'AAA', {'L': 0, 'R': 1}

    while pos != 'ZZZ':
        for instruction in instructions:
            pos = nodes[pos][dirs[instruction]]
            steps += 1

    return steps

def ghost_nodes(instructions:str, nodes:dict[int, tuple[int, int]]) -> int:
    starts, dirs = list(filter(lambda x: x[-1] == 'A', nodes)), {'L': 0, 'R': 1}
    counts = []

    for start in starts:
        pos, steps = start, 0
        while pos[-1] != 'Z':
            for instruction in instructions:
                pos = nodes[pos][dirs[instruction]]
                steps += 1
                if pos[-1] == 'Z':
                    break
        counts.append(steps)

    return math.lcm(*counts)
    """
    while len(list(filter(lambda x: x[-1] == 'Z', pos))) != len(pos):
        for instruction in instructions:
            for p in range(len(pos)):
                pos[p-1] = nodes[pos[p-1]][dirs[instruction]]
            steps += 1

    return steps
    """

if __name__ == '__main__':
    instructions, nodes = parse_input('input')

    # Part 1
    steps = count_steps(instructions, nodes)
    print(f"It took {steps} steps to go from AAA to ZZZ")

    # Part 2
    ghost_steps = ghost_nodes(instructions, nodes)
    print(f"It took {ghost_steps} steps to go from **A to **Z as a ghost")
