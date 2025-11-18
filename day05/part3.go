package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

func main() {
	swords := []sword{}
	data, _ := io.ReadAll(os.Stdin)
	regexp := regexp.MustCompile(`\d+`)
	for line := range strings.Lines(string(data)) {
		numbers := []int{}
		matches := regexp.FindAllString(line, -1)
		for _, match := range matches {
			n, _ := strconv.Atoi(match)
			numbers = append(numbers, n)
		}
		swords = append(swords, sword{numbers[0], spine(numbers[1:])})
	}

	sort.Slice(swords, func(i, j int) bool {
		s1 := swords[i]
		s2 := swords[j]

		q1 := quality(s1.spine)
		q2 := quality(s2.spine)
		if q1 != q2 {
			return q1 > q2
		}

		for level := range s1.spine {
			j1 := join(s1.spine[level])
			j2 := join(s2.spine[level])
			if j1 != j2 {
				return j1 > j2
			}
		}

		return s1.id > s2.id
	})

	checksum := 0
	for i, s := range swords {
		checksum += (i + 1) * s.id
	}
	fmt.Println(checksum)
}

type sword struct {
	id    int
	spine [][]int
}

func spine(numbers []int) [][]int {
	spine := [][]int{}

outer:
	for _, n := range numbers {
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

	return spine
}

func quality(spine [][]int) int {
	q := 0
	for _, s := range spine {
		q *= 10
		q += s[1]
	}
	return q
}

func join(level []int) int {
	r := 0
	for _, n := range level {
		if n != -1 {
			r *= 10
			r += n
		}
	}
	return r
}
