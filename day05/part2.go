package main

import (
	"fmt"
	"io"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	swords := [][]int{}
	data, _ := io.ReadAll(os.Stdin)
	regexp := regexp.MustCompile(`\d+`)
	for line := range strings.Lines(string(data)) {
		sword := []int{}
		matches := regexp.FindAllString(line, -1)
		for _, match := range matches {
			n, _ := strconv.Atoi(match)
			sword = append(sword, n)
		}
		swords = append(swords, sword)
	}

	worst := math.MaxInt
	best := math.MinInt
	for _, sword := range swords {
		q := quality(sword)
		worst = min(worst, q)
		best = max(best, q)
	}
	fmt.Println(best - worst)
}

func quality(sword []int) int {
	spine := [][]int{}

outer:
	for _, n := range sword[1:] {
		for _, s := range spine {
			if s[0] == -1 && n < s[1] {
				s[0] = n
				continue outer
			}
			if s[2] == -1 && n > s[1] {
				s[2] = n
				continue outer
			}
		}
		spine = append(spine, []int{-1, n, -1})
	}

	q := 0
	for _, s := range spine {
		q *= 10
		q += s[1]
	}
	return q
}
