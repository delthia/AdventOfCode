# with open('test-input') as t:
with open('input') as t:
    data = t.read().splitlines()

p = {"X": 1, "Y": 2, "Z": 3, "D": 3, "W": 6, "A": 1, "B": 2, "C": 3}    # Scores
w = ["A Y", "B Z", "C X"]   # Win possibilities

points = 0
for r in data:
    if p[r[0]] == p[r[-1]]:
        points += p[r[-1]] + p["D"]
    elif r in w:
        points += p[r[-1]] + p["W"]
    else:
        points += p[r[-1]]

print(points)

# Second part
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}

points = 0
for r in data:
    if r[-1] == "Z":
        points += p[win[r[0]]] + p["W"]
    elif r[-1] == "Y":
        points += p[draw[r[0]]] + p["D"]
    elif r[-1] == "X":
        points += p[lose[r[0]]]
    else:
        break

print(points)
