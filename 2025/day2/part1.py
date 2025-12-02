def count_range(id_range):
    count = 0
    for i in id_range:
        string = str(i)
        left, right = string[:len(string)//2], string[len(string)//2:]
        if left == right:
            count += i

    return count

with open('input.txt') as f:
    count = 0
    content = f.read().split(',')
    for r in content:
        parts = r.split('-')
        id_range = range(int(parts[0]), int(parts[1]) + 1) # Range includes last
        count += count_range(id_range)
    
    print(count)