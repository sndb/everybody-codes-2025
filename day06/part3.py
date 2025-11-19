from collections import defaultdict

notes = open(0).read().strip() * 1000

window = defaultdict(int)
start, end = -1000, 1001
for c in notes[:end]:
    if c.isupper():
        window[c] += 1

result = 0

for i, c in enumerate(notes):
    if c.islower():
        result += window[c.upper()]

    if 0 <= start < len(notes) and notes[start].isupper():
        window[notes[start]] -= 1

    if 0 <= end < len(notes) and notes[end].isupper():
        window[notes[end]] += 1

    start += 1
    end += 1

print(result)
