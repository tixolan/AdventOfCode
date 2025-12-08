import math
from itertools import combinations

with open('input.txt') as f:
    points = [tuple(int(s) for s in p.split(',')) for p in f.read().splitlines()]
    P1 = 10 if len(points) < 50 else 1000
    circuits = {frozenset([p]) for p in points}
    distances = sorted(combinations(points, 2), key=lambda p: math.dist(*p))

    acc = 0
    for i, (p,q) in enumerate(distances):
        p2 = p[0]*q[0]
        g1, g2 = [next(g for g in circuits if x in g) for x in (p, q)]
        circuits -= {g1, g2}
        circuits.add(g1 | g2)

        if i+1 == P1:
            acc = math.prod(sorted(map(len, circuits), reverse=True)[:3])

        if len(circuits) == 1:
            break

    print(acc)