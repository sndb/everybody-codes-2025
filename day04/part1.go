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
		var f float64
		fmt.Sscanf(line, "%f", &f)
		gears = append(gears, f)
	}

	turns := 2025.0
	for i := 1; i < len(gears); i++ {
		turns *= gears[i-1] / gears[i]
	}
	fmt.Println(int(turns))
}
