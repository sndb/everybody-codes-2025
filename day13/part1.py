import re

numbers = [int(x) for x in re.findall(r"\d+", open(0).read())]

ccw = []
wheel = [1]
for i, n in enumerate(numbers):
    if i % 2 == 0:
        wheel.append(n)
    else:
        ccw.append(n)

wheel += reversed(ccw)
print(wheel[2025 % len(wheel)])
