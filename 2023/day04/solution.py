#!/usr/bin/python3

def parse_input(path:str) -> dict:
    with open(path) as file:
        data = file.read().splitlines()

    games = {}
    for line in data:
        card = line.split(' | ')
        game = card[0].split(': ')[0].split()[1]
        winning = card[0].split(': ')[1].split()
        played = card[1].split()
        games[int(game)] = [winning, played]

    return games

def count_wins(games:dict) -> int:
    points = 0
    for game in games.values():
        gamepoints = 0
        for number in game[0]:
            if number in game[1]:
                if not gamepoints:
                    gamepoints = 1
                else:
                    gamepoints *= 2
        points += gamepoints

    return points

def compute_copies(games:dict) -> int:
    copies = [1 for key in games.keys()]
    for game in range(1, len(copies)+1):
        matches = 0
        for number in games[game][0]:
            if number in games[game][1]:
                matches += 1
            elif matches == len(copies)-game:
                break
        for copy in range(game, game+matches): # game is already offset by one. It starts by being 1
            copies[copy] += 1*copies[game-1]

    return sum(copies)

if __name__ == '__main__':
    # games = parse_input('test-input')
    games = parse_input('input')

    # part 1
    print(f"The total point count is {count_wins(games)}")

    # part 2
    print(f"The total number of copies is {compute_copies(games)}")
