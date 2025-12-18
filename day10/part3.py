from functools import cache

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

@cache
def solve(dragon, sheep, turn):
    if turn == "D":
        result = 0
        r, c = dragon
        for nr, nc in [
            [r - 2, c - 1],
            [r - 2, c + 1],
            [r - 1, c - 2],
            [r - 1, c + 2],
            [r + 1, c - 2],
            [r + 1, c + 2],
            [r + 2, c - 1],
            [r + 2, c + 1],
        ]:
            if 0 <= nr < rows and 0 <= nc < cols:
                if sheep[nc] == nr and grid[nr][nc] != "#":
                    result += solve((nr, nc), sheep[:nc] + (-1,) + sheep[nc + 1 :], "S")
                else:
                    result += solve((nr, nc), sheep, "S")

        return result

    else:
        if all(r == -1 for r in sheep):
            return 1

        result = 0
        for c, r in enumerate(sheep):
            if r == -1 or r + 1 == rows:
                continue

            if (r + 1, c) == dragon and grid[r + 1][c] != "#":
                for nc, nr in enumerate(sheep):
                    if c != nc and 0 <= nr < rows:
                        break
                else:
                    return solve(dragon, sheep, "D")
            else:
                result += solve(dragon, sheep[:c] + (r + 1,) + sheep[c + 1 :], "D")

        return result

dragon = (rows - 1, cols // 2)
sheep = [0 if grid[0][c] == "S" else -1 for c in range(cols)]
print(solve(dragon, tuple(sheep), "S"))
