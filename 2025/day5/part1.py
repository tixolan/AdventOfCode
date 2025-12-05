with open('input.txt') as f:
    content = f.read().splitlines()
    mid = content.index('')
    ranges = [(int(l), int(r)) for l,r in [s.split('-') for s in content[:mid]]]
    ingredients = content[mid+1:]
    count = 0
    for i in ingredients:
        for r in ranges:
            if r[0] <= int(i) <= r[1]:
                count += 1
                break
            

    print(count)