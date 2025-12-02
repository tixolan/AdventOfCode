size = 100

ptr = 50

def run_step(step: str) -> int:
    global ptr

    direction = step[:1]
    distance = int(step[1:])
    if direction == "R": # Higher numbers
        ptr = (ptr + distance) % size
    elif direction == "L": # Lower numbers
        ptr = (ptr - distance) % size
    
    if ptr == 0:
        return 1
    return 0

with open("input.txt") as f:
    steps = f.read().splitlines()
    code = 0
    for step in steps:
        code += run_step(step)

    print(code)