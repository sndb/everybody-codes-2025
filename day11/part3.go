package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	cols := []int{}
	data, _ := io.ReadAll(os.Stdin)
	for line := range strings.Lines(string(data)) {
		n, _ := strconv.Atoi(strings.TrimSpace(line))
		cols = append(cols, n)
	}

	orig := append([]int{}, cols...)

	for {
		done := true
		for i := 1; i < len(cols); i++ {
			if cols[i] > cols[i-1] {
				move := (cols[i] - cols[i-1] + 1) / 2
				cols[i-1] += move
				cols[i] -= move
				done = false
			}
		}
		if done {
			break
		}
	}

	rounds := 0
	for i, c := range cols {
		if c > orig[i] {
			rounds += c - orig[i]
		}
	}
	fmt.Println(rounds)
}
