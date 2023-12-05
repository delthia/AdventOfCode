#!/usr/bin/python3
def parse_input(path:str) -> tuple:
    """
    Saves the input as a list of seeds and a dictionary
    containing a lis for each of the maps
    """
    with open(path) as file:
        almanac = file.read().splitlines()

    seeds = list(map(lambda x: int(x), almanac[0].split()[1:]))
    toint = lambda x: int(x)
    seeds = list(map(toint, almanac[0].split()[1:]))    # Save the seeds in a list
    maps, key = {}, None
    for line in almanac[2:]:
        if 'map' in line:
            key = line.split()[0]
        elif line == '':
            key = None
        else:
            if key not in maps.keys():
                maps[key] = [list(map(toint, line.split()))]
                continue

            maps[key].append(list(map(toint, line.split())))

    return seeds, maps


def calculate_destination(seed:int, ranges:list) -> int:
    """
    Calculates the destination for the seed given the map
    of ranges. If the seed is not in the map, returns seed
    """
    destination = 0
    for r in ranges:
        if r[1] <= seed < r[1]+r[2]:
            return r[0]+seed-r[1]
    return seed

def lowest_location(seeds:list, maps:dict) -> int:
    """
    Calculates the location for each seed and returns
    the lowest value of the calculated locations
    """
    locations = []
    for seed in seeds:
        for m in maps.keys():
            seed = calculate_destination(seed, maps[m])
        locations.append(seed)

    return min(locations)

if __name__ == '__main__':
    # seeds, maps = parse_input('test-input')
    seeds, maps = parse_input('input')

    # Part 1
    print(f"The lowest location number is {lowest_location(seeds, maps)}")

