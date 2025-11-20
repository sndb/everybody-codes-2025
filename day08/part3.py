import itertools
import re

numbers = [int(x) for x in re.findall(r"\d+", open(0).read())]
knots = [sorted(pair) for pair in itertools.pairwise(numbers)]
low, high = min(numbers), max(numbers)
result = 0

for i in range(low, high + 1):
    for j in range(i + 1, high + 1):
        count = 0
        for a, b in knots:
            count += i < a < j < b or a < i < b < j or a == i and b == j
        result = max(result, count)

print(result)
