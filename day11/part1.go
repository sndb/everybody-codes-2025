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

	rounds := 0
	for {
		done := true
		for i := 1; i < len(cols); i++ {
			if cols[i-1] > cols[i] {
				cols[i-1]--
				cols[i]++
				done = false
			}
		}
		if done {
			break
		}
		rounds++
	}

	for {
		if rounds == 10 {
			break
		}
		for i := 1; i < len(cols); i++ {
			if cols[i-1] < cols[i] {
				cols[i-1]++
				cols[i]--
			}
		}
		rounds++
	}

	sum := 0
	for i, c := range cols {
		sum += c * (i + 1)
	}
	fmt.Println(sum)
}
