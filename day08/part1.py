import itertools
import re

numbers = [int(x) for x in re.findall(r"\d+", open(0).read())]
print(sum(abs(a - b) == max(numbers) / 2 for a, b in itertools.pairwise(numbers)))
