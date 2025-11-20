import itertools
import re

numbers = [int(x) for x in re.findall(r"\d+", open(0).read())]
knots = [sorted(pair) for pair in itertools.pairwise(numbers)]
result = sum(
    i < a < j < b or a < i < b < j
    for n, (i, j) in enumerate(knots)
    for a, b in knots[:n]
)
print(result)
