#!/usr/bin/python3

def parse_input(path:str) -> tuple:
    with open(path) as file:
        races = file.read().splitlines()

    # Parse the input
    times = [int(time) for time in races[0].split()[1:]]
    dists = [int(dist) for dist in races[1].split()[1:]]
    races = list(zip(times, dists)) # Combine the two lists into one

    return races

def possible_records(races:list[tuple]) -> list:
    records = [0 for x in range(len(races))]
    for race in races:
        record = race[1]
        for speed in range(race[0]):
            distance = speed * (race[0] - speed)
            if distance > record:
                records[races.index(race)] += 1

    return records

if __name__ == '__main__':
    # races = parse_input('test-input')
    races = parse_input('input')

    records = possible_records(races)
    total = 1
    for record in records:
        total *= record
    print(f"The total number of records multiplied toghether is {total}")
