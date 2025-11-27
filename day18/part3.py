from itertools import combinations_with_replacement
from typing import NamedTuple

class Branch(NamedTuple):
    id: int
    thickness: int

class Plant(NamedTuple):
    thickness: int
    branches: list[Branch]

plants_part, tests_part = open(0).read().split("\n\n\n")

plants = {}
for block in plants_part.split("\n\n"):
    lines = [line.split() for line in block.splitlines()]

    branches = []
    id, thickness = int(lines[0][1]), int(lines[0][4][:-1])
    for words in lines[1:]:
        if words[1] == "free":
            branches.append(Branch(-1, int(words[5])))
        else:
            branches.append(Branch(int(words[4]), int(words[7])))

    plants[id] = Plant(thickness, branches)

tests = []
for line in tests_part.splitlines():
    tests.append([int(x) for x in line.split()])

def calc_energy(id, test):
    if id - 1 < len(test):
        return test[id - 1]

    energy = 0
    plant = plants[id]
    for branch in plant.branches:
        if branch.id == -1:
            energy += branch.thickness
        else:
            energy += branch.thickness * calc_energy(branch.id, test)

    return energy if energy >= plant.thickness else 0

test_results = [calc_energy(len(plants), test) for test in tests]
best_energy = max(test_results)
best_test = tests[test_results.index(best_energy)]

for swaps in combinations_with_replacement(range(len(tests[0])), 4):
    for i in swaps:
        best_test[i] ^= 1

    best_energy = max(best_energy, calc_energy(len(plants), best_test))

    for i in swaps:
        best_test[i] ^= 1

print(sum(best_energy - energy for energy in test_results if energy > 0))
