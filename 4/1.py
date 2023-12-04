#!/usr/bin/python3
import sys
import re

total = 0
for line in sys.stdin:
    winning, mine = line.split("|")
    winning = winning.split(":")[1].strip()
    mine = mine.strip()
    winning = re.sub(r"\s{2,}", " ", winning).split(" ")
    mine = re.sub(r"\s{2,}", " ", mine).split(" ")

    winning = set(map(int, winning))
    mine = set(map(int, mine))
    both = winning.intersection(mine)
    if both:
        total += 2 ** (len(both) - 1)
print(total)
