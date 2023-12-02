#!/usr/bin/python3

def load_data(path:str) -> list:
    """
    Create a dictionary with all the reveals
    in one game for each color
    """
    with open(path) as file:
        data = file.read().splitlines()

    games = []
    for game in data:
        colors = {'red': [], 'green': [], 'blue': []}
        line = game.split(': ')
        for reveal in [x.split(', ') for x in line[1].split('; ')]:
            for color in reveal:
                colors[color.split()[1]].append(int(color.split()[0]))
        games.append({'game': int(line[0].split()[-1]), 'colors': colors})

    return games

if __name__ == '__main__':
    bag, possible = {'red': 12, 'green': 13, 'blue': 14}, []

    # games = load_data('test-input')
    games = load_data('input')

    # Part 1
    for game in games:
        for color in game['colors']:
            if max(game['colors'][color]) > bag[color]:
                break
        else:
            possible.append(game['game'])

    print(f"All the possible games add up to {sum(possible)}")

    # Part 2
    powers = []
    for game in games:
        fewest = [max(game['colors'][color]) for color in game['colors']]
        power = 1
        for pos in fewest:
            power *= pos
        powers.append(power)

    print(f"All the powers add up to {sum(powers)}")
