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

def multiply_records(records:list) -> int:
    total = 1
    for record in records:
        total *= record

    return total

def record_range(time:int, record:int) -> list:
    winning = []
    for speed in range(time):
        distance = speed * (time - speed)
        if distance > record:
            winning.append(speed)
            break

    for speed in range(time, 0, -1):
        distance = speed * (time - speed)
        if distance > record:
            winning.append(speed)
            break

    possible_wins = winning[1] - winning[0] + 1 # Include all the possibilities
    print(f"from {winning[0]} to {winning[1]}")
    return possible_wins

if __name__ == '__main__':
    # races = parse_input('test-input')
    races = parse_input('input')

    # Part 1
    records = possible_records(races)
    total = multiply_records(records)
    print(f"The total number of records multiplied toghether is {total}")

    # Part 2
    print(races)
    time = int(''.join([str(pos[0]) for pos in races]))
    record = int(''.join([str(pos[1]) for pos in races]))
    print(time)
    print(record)
    print("--- Part 2 ---")
    winning = record_range(time, record)
    print(f"You can beat the record {winning} different ways")
