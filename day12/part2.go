package main

import (
	"fmt"
	"io"
	"maps"
	"os"
	"slices"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	grid := strings.Fields(string(data))
	rows := len(grid)
	cols := len(grid[0])

	seen := map[[2]int]bool{{0, 0}: true, {rows - 1, cols - 1}: true}
	queue := slices.Collect(maps.Keys(seen))
	for len(queue) > 0 {
		pos := queue[0]
		queue = queue[1:]

		pr, pc := pos[0], pos[1]
		dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for _, d := range dirs {
			dr, dc := d[0], d[1]
			nr, nc := pr+dr, pc+dc
			if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
				continue
			}

			next := [2]int{nr, nc}
			if grid[nr][nc] <= grid[pr][pc] && !seen[next] {
				queue = append(queue, next)
				seen[next] = true
			}
		}
	}
	fmt.Println(len(seen))
}
