with open('input.txt') as f:
    levels = f.read().splitlines()
    start_level = levels[0]
    beam_idx = start_level.index('S')
    active = [0] * len(start_level)
    active[beam_idx] = 1
    for level in levels[1:]:
        curr_active = active
        for i, a in enumerate(curr_active):
            if a > 0:
                if level[i] == '^':
                    active[i-1] += active[i]
                    active[i+1] += active[i]
                    active[i] = 0
                    
    print(sum(active))
            