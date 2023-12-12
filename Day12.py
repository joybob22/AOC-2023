import sys
import os
import re

def numArrangments(springs, groups):
    if len(groups) == 0 and len(springs) == 0:
        return 1
    if len(springs) == 0 and len(groups) > 0:
        return 0
    if len(groups) == 0 and len(springs) > 0:
        if "#" not in springs:
            return 1
        return 0
    if springs[0] == ".":
        return numArrangments(springs[1:], groups)
    if springs[0] == "#":
        pointer = 1
        while pointer < len(springs) and springs[pointer] != "?" and springs[pointer] != ".":
            pointer += 1
        if pointer == int(groups[0]):
            # We have a valid group. Remove string
            return numArrangments(springs[(pointer+1):], groups[1:])
        if pointer < len(springs) and springs[pointer] == "?":
            return numArrangments(springs[:pointer] + "." + springs[pointer+1:], groups) + numArrangments(springs[:pointer] + "#" + springs[pointer+1:], groups) # Here
        # We don't have a valid group
        return 0
        # return numArrangments(springs[pointer:], groups)
    return numArrangments("." + springs[1:], groups) + numArrangments("#" + springs[1:], groups)

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = re.findall(r"^(.+) (.+)$", contents, re.M)
    totalArrangements = 0
    for springs, groups in rows:
        groups = groups.split(",")
        newNum = numArrangments(springs, groups)
        totalArrangements += newNum
    return totalArrangements

print(part1())