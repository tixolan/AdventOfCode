with open('input.txt') as f:
    content = f.read().splitlines()
    mid = content.index('')
    ranges = [[int(l), int(r)] for l,r in [s.split('-') for s in content[:mid]]]

    count = 0
    prev = -1
    for l, r in sorted(ranges):
        if r <= prev:
            continue

        count += r - max(l, prev + 1) + 1
        prev = max(r, prev)

    print(count)
                