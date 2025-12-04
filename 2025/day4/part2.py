def check_neighbors(lines: list[list[str]], pos: tuple) -> int:
    neighbors = 0
    width = len(lines[0])
    height = len(lines)
    x = pos[0]
    y = pos[1]

    if lines[y][x] == '.':
        return 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if y + i < 0 or x + j < 0 or y + i == height or x + j == width:
                continue
            if lines[y + i][x + j] == '@':
                neighbors += 1

    if neighbors < 4:
        lines[y][x] = '.'
        return 1
    return 0


with open('input.txt') as f:
    lines = [list(line) for line in f.read().splitlines()]
    width = len(lines[0])
    height = len(lines)
    total_rolls = 0

    # First iteration
    rolls = 0
    rolls_removed = False
    for y in range(height):
        for x in range(width):
            rolls += check_neighbors(lines, (x , y))
    if rolls > 0:
        rolls_removed = True
        total_rolls += rolls

    # Other iterations
    while rolls_removed:
        rolls = 0
        rolls_removed = False
        for y in range(height):
            for x in range(width):
                rolls += check_neighbors(lines, (x , y))
        if rolls > 0:
            rolls_removed = True
            total_rolls += rolls
        else:
            rolls_removed = False

    for l in lines:
        for c in l:
            print(c, end='')
        print()

    print(total_rolls)