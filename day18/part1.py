from typing import NamedTuple

class Branch(NamedTuple):
    id: int
    thickness: int

class Plant(NamedTuple):
    thickness: int
    branches: list[Branch]

plants = {}
for block in open(0).read().split("\n\n"):
    lines = [line.split() for line in block.splitlines()]

    branches = []
    id, thickness = int(lines[0][1]), int(lines[0][4][:-1])
    for words in lines[1:]:
        if words[1] == "free":
            branches.append(Branch(-1, int(words[5])))
        else:
            branches.append(Branch(int(words[4]), int(words[7])))

    plants[id] = Plant(thickness, branches)

def calc_energy(id):
    energy = 0
    plant = plants[id]
    for branch in plant.branches:
        if branch.id == -1:
            energy += branch.thickness
        else:
            energy += branch.thickness * calc_energy(branch.id)

    return energy if energy >= plant.thickness else 0

print(calc_energy(len(plants)))
