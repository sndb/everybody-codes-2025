package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	gears := []float64{}
	data, _ := io.ReadAll(os.Stdin)
	for line := range strings.Lines(string(data)) {
		var a, b float64
		if strings.Contains(line, "|") {
			fmt.Sscanf(line, "%f|%f", &a, &b)
			gears = append(gears, a, b)
		} else {
			fmt.Sscanf(line, "%f", &a)
			gears = append(gears, a)
		}
	}

	ratio := 1.0
	for i := 1; i < len(gears); i += 2 {
		ratio *= gears[i-1] / gears[i]
	}
	fmt.Println(int(100 * ratio))
}
