#!/usr/bin/python3
import sys

total = 0

bounds = {"red": 12, "green": 13, "blue": 14}

for line in sys.stdin:
    game, combos = line.split(":")
    game_num = int(game[5:])

    pulls = combos.split(";")
    valid_game = True
    for pull in pulls:
        rgbs = pull.split(",")
        rgbs = [term.strip() for term in rgbs]
        for term in rgbs:
            num, color = term.split(" ")
            num = int(num)
            if num > bounds[color]:
                valid_game = False
                break
        if not valid_game:
            break
    if valid_game:
        total += game_num
print(total)
