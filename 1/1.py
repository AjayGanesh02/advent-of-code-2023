#!/usr/bin/python3
import sys

sum = 0

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
