import itertools

lines = open(0).read().splitlines()
seqs = [line.split(":")[1] for line in lines]
pairs = list(itertools.combinations(seqs, 2))


def similarity(child, parents):
    if child in parents:
        return 0

    s1, s2 = 0, 0
    for c, p1, p2 in zip(child, *parents):
        if c != p1 and c != p2:
            return 0
        s1 += c == p1
        s2 += c == p2
    return s1 * s2


result = sum(max(similarity(seq, pair) for pair in pairs) for seq in seqs)
print(result)
