#!/usr/bin/python3
from collections import defaultdict
import sys
import re
import itertools
import math

total = 0

grid = [line for line in sys.stdin.read().split("\n")]
symbols = {
    (row, col)
    for row, line in enumerate(grid)
    for col, c in enumerate(line)
    if not c.isdigit() and c != "."
}

symbol_to_num: defaultdict[tuple[int, int], list[int]] = defaultdict(list)


def is_valid_coords(r: int, c: int) -> bool:
    return r < len(grid) and r >= 0 and c < (len(grid[0]) - 1) and c >= 0


ds = (-1, 0, 1)
around = list(itertools.product(ds, ds))


def touching_symbol(r: int, c: int) -> set[tuple[int, int]]:
    ret = set()
    for dx, dy in around:
        x, y = r + dx, c + dy
        if is_valid_coords(x, y) and (x, y) in symbols:
            ret.add((x, y))
    return ret


for row, line in enumerate(grid):
    for match in re.finditer(r"\d+", line):
        match_num = int(match.group())
        cur_match_symbols = set()
        for col in range(match.start(), match.end()):
            cur_match_symbols = touching_symbol(row, col).union(cur_match_symbols)
        for symbol in cur_match_symbols:
            symbol_to_num[symbol].append(match_num)

print(
    sum(
        [
            math.prod(part_nums)
            for part_nums in symbol_to_num.values()
            if len(part_nums) == 2
        ]
    )
)
