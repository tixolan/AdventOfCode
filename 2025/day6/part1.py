with open('input.txt') as f:
    lines = [l.split() for l in f.read().splitlines()]
    number_lines = lines[:-1]
    operations = lines[-1]
    total = 0
    for i, op in enumerate(operations):
        if op == '*':
            result = 1
            for numbers in number_lines:
                result *= int(numbers[i])
            total += result
        elif op == '+':
            result = 0
            for numbers in number_lines:
                result += int(numbers[i])
            total += result

    print(total)