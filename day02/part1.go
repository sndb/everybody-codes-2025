package main

import (
	"fmt"
	"os"
)

func main() {
	var a complex
	fmt.Fscanf(os.Stdin, "A=[%d,%d]", &a.x, &a.y)

	r := complex{0, 0}
	for range 3 {
		r = r.mul(r)
		r = r.div(complex{10, 10})
		r = r.add(a)
	}
	fmt.Printf("[%d,%d]\n", r.x, r.y)
}

type complex struct {
	x, y int
}

func (c1 complex) add(c2 complex) complex {
	return complex{c1.x + c2.x, c1.y + c2.y}
}

func (c1 complex) mul(c2 complex) complex {
	return complex{c1.x*c2.x - c1.y*c2.y, c1.x*c2.y + c1.y*c2.x}
}

func (c1 complex) div(c2 complex) complex {
	return complex{c1.x / c2.x, c1.y / c2.y}
}
