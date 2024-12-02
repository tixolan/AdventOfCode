with open("puzzle_input.txt", "r") as puzzle:
    lines = [line.split("   ") for line in puzzle.read().splitlines()]
    data = list(zip(*lines))
    left = data[0]
    right = data[1]

    # Part 1
    acc = 0
    for l, r in zip(sorted(left), sorted(right)):
        acc += abs(int(l) - int(r))
    print("Part 1:", acc)

    # Part 2
    acc = 0
    occurences = {}
    for n in right:
        occurences[n] = occurences.get(n, 0) + 1
    
    for n in left:
        acc += occurences.get(n, 0) * int(n)
    print("Part 2:", acc)