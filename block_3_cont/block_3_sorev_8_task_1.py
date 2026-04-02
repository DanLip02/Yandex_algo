moves = input().strip()
x, y = 0, 0

visits = {(0, 0): 1}

for move in moves:
    if move == "U":
        y += 1
    elif move == "R":
        x += 1
    elif move == "D":
        y -= 1
    elif move == "L":
        x -= 1

    visits[(x, y)] = visits.get((x, y), 0) + 1

result = sum(1 for count in visits.values() if count >= 2)

print(result)