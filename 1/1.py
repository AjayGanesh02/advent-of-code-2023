#!/usr/bin/python3
import sys

sum = 0
nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in sys.stdin:
    first = ""
    for idx, c in enumerate(line):
        if idx >= 3 and line[idx - 3 : idx] in nums:
            first = nums[line[idx - 3 : idx]]
            break
        elif idx >= 4 and line[idx - 4 : idx] in nums:
            first = nums[line[idx - 4 : idx]]
            break
        elif idx >= 5 and line[idx - 5 : idx] in nums:
            first = nums[line[idx - 5 : idx]]
            break
        elif c.isdigit():
            first = c
            break
    # print(first)
    for idx in range(len(line) - 1, -1, -1):
        c = line[idx]
        # print(idx, c)
        if idx + 3 <= len(line) and line[idx : idx + 3] in nums:
            first += nums[line[idx : idx + 3]]
            break
        elif idx + 4 <= len(line) and line[idx : idx + 4] in nums:
            first += nums[line[idx : idx + 4]]
            break
        elif idx + 5 <= len(line) and line[idx : idx + 5] in nums:
            first += nums[line[idx : idx + 5]]
            break
        elif c.isdigit():
            first += c
            break
    # print(first)
    sum += int(first)
print(sum)
