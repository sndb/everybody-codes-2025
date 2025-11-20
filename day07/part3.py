from collections import defaultdict

lines = open(0).read().splitlines()
names = lines[0].split(",")
rules = defaultdict(set)
for line in lines[2:]:
    for next in line[4:].split(","):
        rules[line[0]].add(next)


def combinations(name):
    if len(name) <= 11 and name not in result:
        result.add(name)
        for rule in rules[name[-1]]:
            combinations(name + rule)


result = set()

for name in names:
    for i in range(len(name) - 1):
        if name[i + 1] not in rules[name[i]]:
            break
    else:
        combinations(name)

print(sum(len(name) >= 7 for name in result))
