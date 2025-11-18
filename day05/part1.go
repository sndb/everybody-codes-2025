package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
)

func main() {
	numbers := []int{}
	data, _ := io.ReadAll(os.Stdin)
	regexp := regexp.MustCompile(`\d+`)
	matches := regexp.FindAllString(string(data), -1)
	for _, match := range matches {
		n, _ := strconv.Atoi(match)
		numbers = append(numbers, n)
	}

	spine := [][]int{}

outer:
	for _, n := range numbers[1:] {
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

	for _, s := range spine {
		fmt.Print(s[1])
	}
	fmt.Println()
}
