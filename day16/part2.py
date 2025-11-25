wall = [int(x) for x in input().split(",")]

i = 1
spell = []
result = 1
for w in wall:
    if sum(i % x == 0 for x in spell) < w:
        spell.append(i)
        result *= i
    i += 1

print(result)
