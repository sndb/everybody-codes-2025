spell = [int(x) for x in input().split(",")]
print(sum((i + 1) % x == 0 for i in range(90) for x in spell))
