wall = [int(x) for x in input().split(",")]

i = 1
spell = []
for w in wall:
    if sum(i % x == 0 for x in spell) < w:
        spell.append(i)
    i += 1

target = 202520252025000
l, r = 0, target
while l <= r:
    m = (l + r) // 2
    if sum(m // x for x in spell) > target:
        r = m - 1
    else:
        l = m + 1

print(r)
