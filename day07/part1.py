from collections import defaultdict

lines = open(0).read().splitlines()
names = lines[0].split(",")
rules = defaultdict(set)
for line in lines[2:]:
    for next in line[4:].split(","):
        rules[line[0]].add(next)

for name in names:
    for i in range(len(name) - 1):
        if name[i + 1] not in rules[name[i]]:
            break
    else:
        print(name)
