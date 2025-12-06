import math

with open('input.txt') as f:
    lines = f.read().splitlines()
    operations = lines[-1]
    total = 0

    numbers = []
    curr_op = ''
    for i, op in enumerate(operations):
        s = [l[i] for l in lines]
        if s.count(' ') == len(s):
            if curr_op == '*':
                total += math.prod(numbers)
            elif curr_op == '+':
                total += sum(numbers)
            continue

        if op == '*' or op == '+':
            numbers = []
            curr_op = op
        
        number = ''
        for c in s:
            if c.isnumeric():
                number += c
        numbers.append(int(number))
    
    if curr_op == '*':
        total += math.prod(numbers)
    elif curr_op == '+':
        total += sum(numbers)

    print(total)