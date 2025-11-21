import itertools

lines = open(0).read().splitlines()
seqs = [line.split(":")[1] for line in lines]
pairs = list(itertools.combinations(seqs, 2))
results = sorted(sum(a == b for a, b in zip(s1, s2)) for s1, s2 in pairs)

print(results[1] * results[2])
