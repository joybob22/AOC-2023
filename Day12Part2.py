import sys
import os
import re

# knownArrangements = {}

def numArrangments(springs, groups, knownArrangements):
    if springs + str(groups) in knownArrangements:
        return knownArrangements[springs + str(groups)]
    if len(groups) == 0 and len(springs) == 0:
        return 1
    if len(springs) == 0 and len(groups) > 0:
        return 0
    if len(groups) == 0 and len(springs) > 0:
        if "#" not in springs:
            return 1
        return 0
    if springs[0] == ".":
        result = numArrangments(springs[1:], groups, knownArrangements)
        knownArrangements[springs[1:] + str(groups)] = result
        return result
    if springs[0] == "#":
        pointer = 1
        while pointer < len(springs) and springs[pointer] != "?" and springs[pointer] != ".":
            pointer += 1
        if pointer == int(groups[0]):
            # We have a valid group. Remove string
            result = numArrangments(springs[(pointer+1):], groups[1:], knownArrangements)
            knownArrangements[springs[(pointer+1):] + str(groups[1:])] = result
            return result
        if pointer < len(springs) and springs[pointer] == "?":
            result1 = numArrangments(springs[:pointer] + "." + springs[pointer+1:], groups, knownArrangements)
            result2 = numArrangments(springs[:pointer] + "#" + springs[pointer+1:], groups, knownArrangements)
            knownArrangements[springs[:pointer] + "." + springs[pointer+1:] + str(groups)] = result1
            knownArrangements[springs[:pointer] + "#" + springs[pointer+1:] + str(groups)] = result2
            return result1 + result2
        # We don't have a valid group
        return 0
    result1 = numArrangments("." + springs[1:], groups, knownArrangements)
    result2 = numArrangments("#" + springs[1:], groups, knownArrangements)
    knownArrangements["." + springs[1:] + str(groups)] = result1
    knownArrangements["#" + springs[1:] + str(groups)] = result2
    return result1 + result2

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = re.findall(r"^(.+) (.+)$", contents, re.M)
    totalArrangements = 0
    knownArrangements = {}
    for springs, groups in rows:
        knownArrangements.clear()
        groups = groups.split(",") * 5
        springs = (springs + "?") * 5
        springs = springs[:len(springs)-1]
        newNum = numArrangments(springs, groups, knownArrangements)
        totalArrangements += newNum
    return totalArrangements

print(part2())