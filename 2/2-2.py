#!/usr/bin/python3
import sys

total = 0

for line in sys.stdin:
    bounds = {"red": 0, "green": 0, "blue": 0}
    combos = line.split(":")[1]

    pulls = combos.split(";")
    for pull in pulls:
        rgbs = pull.split(",")
        rgbs = [term.strip() for term in rgbs]
        for term in rgbs:
            num, color = term.split(" ")
            num = int(num)
            bounds[color] = max(bounds[color], num)
    acc = 1
    for color, num in bounds.items():
        acc *= num
    total += acc


print(total)
