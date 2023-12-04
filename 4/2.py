#!/usr/bin/python3
import sys
import re

wins = []
copies = []
for idx, line in enumerate(sys.stdin):
    winning, mine = line.split("|")
    winning = winning.split(":")[1].strip()
    mine = mine.strip()
    winning = re.sub(r"\s{2,}", " ", winning).split(" ")
    mine = re.sub(r"\s{2,}", " ", mine).split(" ")

    winning = set(map(int, winning))
    mine = set(map(int, mine))
    both = winning.intersection(mine)
    wins.append(len(both))
    copies.append(1)
for idx, win in enumerate(wins):
    for i in range(1, win + 1):
        copies[idx + i] += copies[idx]
print(sum(copies))
