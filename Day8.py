import re
import os
import sys
import functools
from math import lcm

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r"^\w+$"
    instructions = re.findall(pattern, contents, re.M)[0]

    pattern = r"^(\w+) = \((\w+), (\w+)\)$"
    data = re.findall(pattern, contents, re.M)

    lookupTable = {}

    for key, left, right in data:
        lookupTable[key] = [left, right]
    
    currentKey = "AAA"
    stepsTaken = 0

    while currentKey != "ZZZ":
        instruction = 0 if instructions[stepsTaken % len(instructions)] == "L" else 1
        currentKey = lookupTable[currentKey][instruction]
        stepsTaken += 1
    
    return stepsTaken

# print(part1())

def lcmOfList(someList):
    result = someList[0] 
    for i in range(1, len(someList)):
        result = lcm(result, someList[i])
    return result

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r"^\w+$"
    instructions = re.findall(pattern, contents, re.M)[0]

    pattern = r"^(\w+) = \((\w+), (\w+)\)$"
    data = re.findall(pattern, contents, re.M)

    lookupTable = {}
    currentKeys = []

    for key, left, right in data:
        lookupTable[key] = [left, right]
        if key[2] == "A":
            currentKeys.append(key)
    
    stepsTaken = [0] * len(currentKeys)

    for i, key in enumerate(currentKeys):
        currentKey = key
        while currentKey[2] != "Z":
            instruction = 0 if instructions[stepsTaken[i] % len(instructions)] == "L" else 1
            currentKey = lookupTable[currentKey][instruction]
            stepsTaken[i] += 1

    return lcmOfList(stepsTaken)

print(part2())


    

# print(lcmOfList([4,3,2]))