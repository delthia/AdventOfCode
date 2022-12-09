# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

pos = [0, 0]
positions = []
for step in range(0, len(data)):
    move = data[step]
    for ms in range(0, int(move.split(' ')[-1])): # Had to cheat a little bit. What an oversight. https://www.reddit.com/r/adventofcode/comments/zgrl4c/2022_day_9_part_1_stuck/
        if move[0] == 'R':
            pos[0] += 1
        elif move[0] == 'L':
            pos[0] -= 1
        elif move[0] == 'U':
            pos[1] += 1
        elif move[0] == 'D':
            pos[1] -= 1
        positions.append(pos[:])

tail = [0, 0]
tails = []
for head in positions:
    if head[0] - tail[0] == 2:
        tail[0] += 1
        if head[1] - tail[1] == 1:
            tail[1] += 1
        elif tail[1] - head[1] == 1:
            tail[1] -= 1
    elif tail[0] - head[0] == 2:
        tail[0] -= 1
        if head[1] - tail[1] == 1:
            tail[1] += 1
        elif tail[1] - head[1] == 1:
            tail[1] -= 1
    elif head[1] - tail[1] == 2:
        tail[1] += 1
        if head[0] - tail[0] == 1:
            tail[0] += 1
        elif tail[0] - head[0] == 1:
            tail[0] -= 1
    elif tail[1] - head[1] == 2:
        tail[1] -= 1
        if head[0] - tail[0] == 1:
            tail[0] += 1
        elif tail[0] - head[0] == 1:
            tail[0] -= 1
    tails.append(tail[:])
    
unique = []
for t in tails:
    if t not in unique:
        unique.append(t[:])
print(len(unique))
