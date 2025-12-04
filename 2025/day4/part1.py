def check_neighbors(lines: list[str], pos: tuple) -> int:
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
        return 1
    return 0


with open('input.txt') as f:
    lines = f.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    rolls = 0
    for y in range(height):
        for x in range(width):
            rolls += check_neighbors(lines, (x , y))
    print(rolls)