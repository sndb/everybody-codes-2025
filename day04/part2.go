package main

import (
	"fmt"
	"io"
	"math"
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

	ratio := 1.0
	for i := 1; i < len(gears); i++ {
		ratio *= gears[i-1] / gears[i]
	}
	fmt.Println(int(math.Ceil(10000000000000 / ratio)))
}
