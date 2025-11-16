package main

import (
	"fmt"
	"io"
	"os"
	"slices"
	"strings"
)

func main() {
	data, _ := io.ReadAll(os.Stdin)
	lines := slices.Collect(strings.Lines(string(data)))
	names := strings.Split(strings.TrimSpace(lines[0]), ",")
	moves := strings.Split(strings.TrimSpace(lines[2]), ",")

	for _, move := range moves {
		var dir byte
		var count int
		fmt.Sscanf(move, "%c%d", &dir, &count)

		if dir == 'L' {
			count = -count
		}

		pos := count % len(names)
		if pos < 0 {
			pos += len(names)
		}

		names[0], names[pos] = names[pos], names[0]
	}

	fmt.Println(names[0])
}
