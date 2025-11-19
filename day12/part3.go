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

	result := map[[2]int]bool{}
	for range 3 {
		var best map[[2]int]bool
		for r := 0; r < rows; r++ {
			for c := 0; c < cols; c++ {
				orig := [2]int{r, c}
				if result[orig] {
					continue
				}

				seen := map[[2]int]bool{orig: true}
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
						if grid[nr][nc] <= grid[pr][pc] && !result[next] && !seen[next] {
							queue = append(queue, next)
							seen[next] = true
						}
					}
				}

				if len(seen) > len(best) {
					best = seen
				}
			}
		}
		for pos := range best {
			result[pos] = true
		}
	}
	fmt.Println(len(result))
}
