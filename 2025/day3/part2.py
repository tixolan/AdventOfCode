def obtain_largest_joltage(battery_bank: str) -> int:
    battery_amount = 12
    buffer = list('0' * battery_amount)
    index = 0

    for i in range(battery_amount):
        start = index
        candidates = battery_bank[index:-(battery_amount - i - 1)]
        for j, battery in enumerate(candidates):
            if battery > buffer[i]:
                index = start + j + 1
                buffer[i] = battery
    
    # Deal with the last digit
    candidates = battery_bank[index:]
    for j, battery in enumerate(candidates):
        if battery > buffer[i]:
            buffer[i] = battery

    return int(''.join(buffer))


with open('input.txt') as f:
    battery_banks = f.read().splitlines()
    total_joltage = 0
    for battery_bank in battery_banks:
        total_joltage += obtain_largest_joltage(battery_bank)
    
    print(total_joltage)