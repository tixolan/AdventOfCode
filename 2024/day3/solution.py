import re

with open("puzzle_input.txt", "r") as puzzle:
    content = puzzle.read()
    pattern_mul = r"mul\(\d{1,3},\s*\d{1,3}\)"
    pattern = r"(?:don't\(\)|do\(\)|mul\(\d{1,3},\s*\d{1,3}\))"

    # Part 1
    muls = re.findall(pattern_mul, content) 
    acc = 0
    for mul in muls:
        ops = mul[4:-1].split(",")
        acc += int(ops[0]) * int(ops[1])
    print("Part 1:", acc)

    matches = re.findall(pattern, content)
    should_add = True
    acc = 0
    for match in matches:
        if match == "do()":
            should_add = True
        elif match == "don't()":
            should_add = False
        else:
            if should_add:
                ops = match[4:-1].split(",")
                acc += int(ops[0]) * int(ops[1])
    print("Part 2:", acc)