import re
import os
import sys

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r" +(\d+) +(\d+) +(\d+) *(\d+)?"
    inputRows = re.findall(pattern, contents, re.M)

    multipliedSolutionPossibilities = 1
    for i, time in enumerate(inputRows[0]):
        if time == "":
            continue
        distance = int(inputRows[1][i])
        possibleSolutions = 0
        for velocity in range(1,int(time)):
            traveledDistance = velocity * (int(time) - velocity)
            if traveledDistance > distance:
                possibleSolutions += 1
        multipliedSolutionPossibilities *= possibleSolutions
    
    return multipliedSolutionPossibilities


# print(part1())

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r" +(\d+) +(\d+) +(\d+) *(\d+)?"
    inputRows = re.findall(pattern, contents, re.M)

    time = "".join(inputRows[0])
    distance = "".join(inputRows[1])
    
    possibleSolutions = 0
    for velocity in range(1,int(time)):
        traveledDistance = velocity * (int(time) - velocity)
        if traveledDistance > int(distance):
            possibleSolutions += 1
    
    return possibleSolutions

print(part2())