import sys
import os
import re

class NumberContainer():
    def __init__(self, num) -> None:
        self.num = num
        self.changed = False

class CustomRange():
    def __init__(self, lowerLimit, upperLimit) -> None:
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
    
    def contains(self, num):
        # Range [lowerLimit, upperLimit)
        return num >= self.lowerLimit and num < self.upperLimit

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    sections = contents.split("\n\n")

    seeds = sections.pop(0)
    pattern = r"\d+"
    seedNums = re.findall(pattern, seeds, re.M)
    numsInQuestion = []

    for seedNum in seedNums:
        numsInQuestion.append(NumberContainer(int(seedNum)))

    pattern = r"^(\d+) (\d+) (\d+)$"
    for section in sections:
        nums = re.findall(pattern, section, re.M)
        for destinationStart, sourceStart, rangeLength in nums:
            difference = int(destinationStart) - int(sourceStart)
            theRange = CustomRange(int(sourceStart), (int(sourceStart) + int(rangeLength)))
            for numContainer in numsInQuestion:
                if numContainer.changed == False and theRange.contains(numContainer.num):
                    numContainer.num += difference
                    numContainer.changed = True
        for numContainer in numsInQuestion:
            numContainer.changed = False

    smallestLocation = numsInQuestion.pop(0).num
    for numContainer in numsInQuestion:
        if numContainer.num < smallestLocation:
            smallestLocation = numContainer.num
    
    return smallestLocation

# print(part1())

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    sections = contents.split("\n\n")

    seeds = sections.pop(0)
    pattern = r"\d+"
    seedNums = re.findall(pattern, seeds, re.M)
    numsInQuestion = []

    for i in range(int(len(seedNums) / 2)):
        pointer = i * 2
        for j in range(int(seedNums[pointer+1])):
            numsInQuestion.append(NumberContainer(int(seedNums[pointer]) + j))

    pattern = r"^(\d+) (\d+) (\d+)$"
    for section in sections:
        nums = re.findall(pattern, section, re.M)
        for destinationStart, sourceStart, rangeLength in nums:
            difference = int(destinationStart) - int(sourceStart)
            theRange = CustomRange(int(sourceStart), (int(sourceStart) + int(rangeLength)))
            for numContainer in numsInQuestion:
                if numContainer.changed == False and theRange.contains(numContainer.num):
                    numContainer.num += difference
                    numContainer.changed = True
        for numContainer in numsInQuestion:
            numContainer.changed = False

    smallestLocation = numsInQuestion.pop(0).num
    for numContainer in numsInQuestion:
        if numContainer.num < smallestLocation:
            smallestLocation = numContainer.num
    
    return smallestLocation

print(part2())