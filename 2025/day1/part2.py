size = 100
ptr = 50

def run_step(step: str) -> int:
    global ptr

    start = ptr
    direction = step[:1]
    distance = int(step[1:])
    zeroes = 0

    if direction == "R":
        ptr = (ptr + distance) % size
    elif direction == "L":
        start = (size - start) % size
        ptr = (ptr - distance) % size

    range_modulo = distance % size
    zeroes += (start + range_modulo) // size + distance // size

    return zeroes

with open("input.txt") as f:
    steps = f.read().splitlines()
    code = 0
    for step in steps:
        code += run_step(step)

    print(code)