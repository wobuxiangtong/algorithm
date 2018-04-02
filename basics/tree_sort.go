package main

import (
	"fmt"
	"io"
	"os"
)

type tree struct {
	value       int
	left, right *tree
}

func sort(values []int) {
	var root *tree
	for _, v := range values {
		root = add(root, v)
	}
	appendValues(values[:0], root)
}

func appendValues(values []int, t *tree) []int {
	if t != nil {
		values = appendValues(values, t.left)
		values = append(values, t.value)
		values = appendValues(values, t.right)
	}

	return values
}

func add(t *tree, v int) *tree {
	if t == nil {
		t = new(tree)
		t.value = v
		return t
	}

	if v < t.value {
		t.left = add(t.left, v)
	} else {
		t.right = add(t.right, v)
	}
	return t
}

func main() {
	// a := []int{1, 23, 34, 54, 22, 12, 34, 25}
	// sort(a)
	// fmt.Println(a)
	// test(a...)

	// var c BytesCounter
	// c.Write([]byte("hello"))
	// fmt.Println(c)
	// var name = "Dolly"
	// fmt.Fprintf(&c, "hello,%s", name)
	// fmt.Println(c)
	os.Stdout.Write([]byte("hello"))
	os.Stdout.Close()
	var w io.Writer
	w = os.Stdout
	w.Write([]byte("hello"))

}

func test(a ...int) {
	fmt.Println(a)
}

type BytesCounter int64

func (c *BytesCounter) Write(p []byte) (int, error) {
	*c = 0
	*c += BytesCounter(int64(len(p)))
	return len(p), nil
}

func CounterWriter(w io.Writer) (io.Writer, *int64) {

	return w
}
