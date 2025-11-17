package main

import (
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	crates := []int{}
	data, _ := io.ReadAll(os.Stdin)
	for s := range strings.SplitSeq(strings.TrimSpace(string(data)), ",") {
		n, _ := strconv.Atoi(s)
		crates = append(crates, n)
	}

	sort.Ints(crates)

	result := 0
	for i, c := range crates {
		if i == 0 || c != crates[i-1] {
			result += c
		}
	}
	fmt.Println(result)
}
