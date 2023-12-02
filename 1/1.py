#!/usr/bin/python3
import sys

sum = 0
nums = {
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

for line in sys.stdin:
    first = ""
    for c in line:
        if c.isdigit():
            first = c
            break
    for c in reversed(line):
        if c.isdigit():
            first += c
            break
    sum += int(first)
print(sum)
