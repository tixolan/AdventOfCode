def obtain_largest_joltage(battery_bank: str) -> int:
    largest_left = "0"
    index = 0
    for i, battery in enumerate(battery_bank[:-1]):
        if battery > largest_left:
            index = i
            largest_left = battery
    
    largest_right = "0"
    for battery in battery_bank[index+1:]:
        if battery > largest_right:
            largest_right = battery

    return int(largest_left + largest_right)


with open('input.txt') as f:
    battery_banks = f.read().splitlines()
    total_joltage = 0
    for battery_bank in battery_banks:
        total_joltage += obtain_largest_joltage(battery_bank)
    
    print(total_joltage)