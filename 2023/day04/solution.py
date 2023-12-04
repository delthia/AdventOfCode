#!/usr/bin/python3

def parse_input(path:str) -> ...:
    with open(path) as file:
        data = file.read().splitlines()

    games = []
    for line in data:
        card = line.split(' | ')
        winning = card[0].split(': ')[1].split()
        played = card[1].split()
        games.append([winning, played])

    return games

def count_wins(games:list) -> ...:
    points = 0
    for game in games:
        gamepoints = 0
        for number in game[0]:
            if number in game[1]:
                if gamepoints == 0:
                    gamepoints += 1
                else:
                    gamepoints *= 2
        points += gamepoints

    return points

if __name__ == '__main__':
    # games = parse_input('test-input')
    games = parse_input('input')
    print(f"The total point count is {count_wins(games)}")
