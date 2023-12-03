with open('input.txt') as f:
	lines = f.read()

print(lines)

word_pairs = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

result = 0

for line in lines.strip().split("\n"):
    first = None
    last = None
    s = ""

    for char in line:
        digit = None
        if char.isdigit():
            digit = char
        else:
            s += char;

            for word, num in word_pairs.items():
                if s.endswith(word):
                    digit = str(num)
        if digit is not None:
            last = digit
            if first is None:
                first = digit

    result += int(first+last)
    print(first, last)

print(result)