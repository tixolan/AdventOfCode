def count_range(id_range):
    count = 0
    for i in id_range:
        string = str(i)
        ptr = 1
        buffer = string[0]
        while ptr + len(buffer) <= len(string):
            to_compare = string[ptr:ptr+len(buffer)]
            if to_compare == buffer: # Repeated once, let's see if invalid ID
                valid = True
                for l in range(0, len(string), len(buffer)):
                    to_compare = string[l:l+len(buffer)]
                    if to_compare != buffer:
                        valid = False
                if valid:
                    count += i
                    break
            ptr += 1
            buffer = string[:ptr]

    return count

with open('input.txt') as f:
    count = 0
    content = f.read().split(',')
    for r in content:
        parts = r.split('-')
        id_range = range(int(parts[0]), int(parts[1]) + 1) # Range includes last
        count += count_range(id_range)
    
    print(count)

4174379265