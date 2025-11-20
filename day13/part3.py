import re

numbers = [int(x) for x in re.findall(r"\d+", open(0).read())]
ranges = list(zip(numbers[0::2], numbers[1::2]))

ccw = []
wheel = [1]
for i, (a, b) in enumerate(ranges):
    if i % 2 == 0:
        wheel += range(a, b + 1)
    else:
        ccw += range(a, b + 1)

wheel += reversed(ccw)
print(wheel[202520252025 % len(wheel)])
