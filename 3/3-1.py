#!/usr/bin/python3
import sys

total = 0

grid = [[c for c in line] for line in sys.stdin.readlines()]
grid[-1].append("\n")


def is_valid_coords(r: int, c: int) -> bool:
    return r < len(grid) and r >= 0 and c < (len(grid[0]) - 1) and c >= 0


def touching_symbol(r: int, c: int) -> bool:
    around: list[tuple[int, int]] = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for dx, dy in around:
        x, y = r + dx, c + dy
        if is_valid_coords(x, y) and not grid[x][y].isdigit() and grid[x][y] != ".":
            return True
    return False


for row, line in enumerate(grid):
    cur_num = ""
    valid = False
    for col, c in enumerate(line):
        if c.isdigit():
            cur_num += c
            if touching_symbol(row, col):
                valid = True
        else:
            if cur_num != "" and valid:
                total += int(cur_num)
            cur_num = ""
            valid = False

print(total)
