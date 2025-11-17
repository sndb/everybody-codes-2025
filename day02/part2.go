package main

import (
	"fmt"
	"os"
)

func main() {
	var a complex
	fmt.Fscanf(os.Stdin, "A=[%d,%d]", &a.x, &a.y)

	engraved := 0
	for y := a.y; y <= a.y+1000; y += 10 {
	next:
		for x := a.x; x <= a.x+1000; x += 10 {
			r := complex{0, 0}
			for range 100 {
				r = r.mul(r)
				r = r.div(complex{100000, 100000})
				r = r.add(complex{x, y})
				if -1000000 > r.x || r.x > 1000000 || -1000000 > r.y || r.y > 1000000 {
					continue next
				}
			}
			engraved++
		}
	}
	fmt.Println(engraved)
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
