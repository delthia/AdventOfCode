#!/usr/bin/python3

def parse_input(path:str) -> list[tuple]:
    with open(path) as file:
        games = file.read().splitlines()

    return [(game.split()[0], game.split()[1]) for game in games]

def calculate_type(hands:list[tuple], joker:bool = False) -> dict:
    types = [[] for x in range(7)]
    for hand in hands:
        cards = hand[0]
        # distribution = sorted([cards.count(x) for x in unique])

        if joker and 'J' in hand[0]:
            h = ''.join(list(filter(lambda x: x != 'J', hand[0])))
            unique = set(h)

            distribution = [cards.count(x) for x in unique]

            if distribution != []:
                distribution[distribution.index(max(distribution))] += cards.count('J')
                distribution.sort()
            else:
                distribution.append(5)
        else:
            unique = set(hand[0])
            distribution = sorted([cards.count(x) for x in unique])

        match distribution:
            case [5]:
                types[0].append(cards)
                # print('five of a kind')
            case [1, 4]:
                types[1].append(cards)
                # print('four of a kind')
            case [2, 3]:
                types[2].append(cards)
                # print('full house')
            case [1, 1, 3]:
                types[3].append(cards)
                # print('three of a kind')
            case [1, 2, 2]:
                types[4].append(cards)
                # print('two pair')
            case [1, 1, 1, 2]:
                types[5].append(cards)
                # print('one pair')
            case [1, 1, 1, 1, 1]:
                types[6].append(cards)
                # print('high hand')

    return types

def sort_types(types:dict, order:list) -> list[list]:
    ranked = []
    for t in reversed(types):
        for hand in sorted(t, key=lambda word: [order.index(c) for c in word]):
            ranked.append(hand)

    return ranked

def winnings(hands:list[tuple], ranked:list) -> int:
    total_winnings = 0
    for hand in hands:
        total_winnings += (ranked.index(hand[0])+1) * int(hand[1])

    return total_winnings

if __name__ == '__main__':
    strengths = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    # hands = parse_input('test-input')
    hands = parse_input('input')

    """
          hand      |  id
    -----------------------
     Five of a kind |  0
     Four of a kind |  1
       Full house   |  2
    Three of a kind |  3
        Two pair    |  4
        One pair    |  5
        High card   |  6
    """
    types = calculate_type(hands)
    ranked = sort_types(types, strengths)
    print(f"Total winnings: {winnings(hands, ranked)}")

    # Part 2
    strengths = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')
    types = calculate_type(hands, True)
    ranked = sort_types(types, strengths)
    print(f"--- Part 2 ---\nTotal winnings with joker: {winnings(hands, ranked)}")
