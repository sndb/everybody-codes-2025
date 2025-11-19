from collections import defaultdict

notes = open(0).read().strip()
mentors = defaultdict(int)
result = 0

for c in notes:
    if c.isupper():
        mentors[c] += 1
    elif c == "a":
        result += mentors["A"]

print(result)
