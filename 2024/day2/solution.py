def is_safe(levels):
    increasing = levels[0] < levels[1]
    safe = True
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i] if increasing else levels[i] - levels[i + 1]
        if diff not in diffs:
            safe = False
            break
    return safe

with open("puzzle_input.txt", "r") as puzzle:
    level_reports = puzzle.read().splitlines()
    diffs = (1, 2, 3)
    acc = 0
    for report in level_reports:
        levels = list(map(lambda x: int(x), report.split(" ")))
        increasing = levels[0] < levels[1]
        safe = is_safe(levels)
        if safe: acc += 1
    print("Part 1:", acc)

    acc = 0
    for report in level_reports:
        levels = list(map(lambda x: int(x), report.split(" ")))
        safe = is_safe(levels)
        if safe: acc += 1
        else:
            safe = False
            for i in range(len(levels)):
                new_levels = [levels[j] for j in range(len(levels)) if j != i]
                safe = is_safe(new_levels)
                if safe:
                    break
            if safe: acc += 1
    print("Part 2:", acc)
            
