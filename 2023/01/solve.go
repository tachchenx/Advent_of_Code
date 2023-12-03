package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"unicode"
)

func main() {
	f, err := os.Open("input.txt")
	var lines [][]rune
	var ans int

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		line := []rune(scanner.Text())
		lines = append(lines, line)
	}

	for _, line := range lines {
		fmt.Println(string(line))

		var first rune
		for _, char := range line {
			if unicode.IsDigit(char) {
				first = char
				break
			}
		}

		var last rune
		for _, char := range line {
			if unicode.IsDigit(char) {
				last = char
			}
		}
		fmt.Print(string(first))
		fmt.Print(string(last))
		fmt.Println("")

		sum := string(first) + string(last)
		num, error := strconv.Atoi(sum)

		if error != nil {
			fmt.Println("Error converting string to integer:", err)
			return
		}

		ans += num
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("The answer is: ", ans)
}
