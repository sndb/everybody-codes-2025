import itertools
from collections import defaultdict

lines = open(0).read().splitlines()
seqs = {int(scale): seq for scale, seq in (line.split(":") for line in lines)}
pairs = list(itertools.combinations(seqs.keys(), 2))


def similarity(child, parent1, parent2):
    s1, s2 = 0, 0
    for i, c in enumerate(child):
        if c != parent1[i] and c != parent2[i]:
            return 0
        s1 += c == parent1[i]
        s2 += c == parent2[i]
    return s1 * s2


relations = defaultdict(set)
for child in seqs:
    max_s = 0
    parent1 = 0
    parent2 = 0
    for p1, p2 in pairs:
        if child != p1 and child != p2:
            s = similarity(seqs[child], seqs[p1], seqs[p2])
            if s > max_s:
                max_s = s
                parent1 = p1
                parent2 = p2

    if max_s > 0:
        for p in (parent1, parent2):
            relations[child].add(p)
            relations[p].add(child)

result = 0
seen = set()
for seq in seqs:
    if seq in seen:
        continue

    family = set()
    queue = [seq]
    while queue:
        member = queue.pop()
        family.add(member)
        for rel in relations[member]:
            if rel not in family:
                queue.append(rel)
                family.add(rel)

    seen |= family
    result = max(result, sum(family))

print(result)
