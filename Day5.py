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
        self.changed = False
    
    def contains(self, num):
        # Range [lowerLimit, upperLimit)
        return num >= self.lowerLimit and num < self.upperLimit
    
    def rangeContainsRange(self, range):
        check1 = (range.lowerLimit >= self.lowerLimit and range.lowerLimit < self.upperLimit) or (range.upperLimit <= self.upperLimit and range.upperLimit > self.lowerLimit)
        check2 = (self.lowerLimit >= range.lowerLimit and self.lowerLimit < range.upperLimit) or (self.upperLimit <= range.upperLimit and self.upperLimit > range.lowerLimit)
        return check1 or check2
    
    def splitOutOfRange(self, aRange):
        # Assuming rangeContainsRange has been checked before this function call
        newRanges = []
        newRangeUpperLimit = aRange.upperLimit if aRange.upperLimit < self.upperLimit else self.upperLimit
        newRangeLowerLimit = aRange.lowerLimit if aRange.lowerLimit > self.lowerLimit else self.lowerLimit
        newRange = CustomRange(newRangeLowerLimit, newRangeUpperLimit)
        newRange.changed = True
        newRanges.append(newRange)
        if newRange.lowerLimit > self.lowerLimit:
            newRanges.append(CustomRange(self.lowerLimit, newRange.lowerLimit))
        if newRange.upperLimit < self.upperLimit:
            newRanges.append(CustomRange(newRange.upperLimit, self.upperLimit))
        return newRanges
    
    def prettyString(self):
        return str(self.lowerLimit) + "..<" + str(self.upperLimit)


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
    rangesInQuestion = []

    for i in range(int(len(seedNums) / 2)):
        pointer = i * 2
        rangesInQuestion.append(CustomRange(int(seedNums[pointer]), int(seedNums[pointer]) + int(seedNums[pointer+1])))

    pattern = r"^(\d+) (\d+) (\d+)$"
    for section in sections:
        nums = re.findall(pattern, section, re.M)
        for destinationStart, sourceStart, rangeLength in nums:
            difference = int(destinationStart) - int(sourceStart)
            theRange = CustomRange(int(sourceStart), (int(sourceStart) + int(rangeLength)))
            changedRangeIndexs = []
            for (i, rangeInQuestion) in enumerate(rangesInQuestion):
                if rangeInQuestion.changed == False and rangeInQuestion.rangeContainsRange(theRange):
                    newRanges = rangeInQuestion.splitOutOfRange(theRange)
                    for subRange in newRanges:
                        if subRange.changed:
                            subRange.upperLimit += difference
                            subRange.lowerLimit += difference
                        rangesInQuestion.append(subRange)
                    changedRangeIndexs.append(i)
            numRemovals = 0
            for index in changedRangeIndexs:
                rangesInQuestion.pop(index-numRemovals)
                numRemovals+=1
        for rangeContainer in rangesInQuestion:
            rangeContainer.changed = False

    smallestLocation = rangesInQuestion.pop(0).lowerLimit
    for subRange in rangesInQuestion:
        if subRange.lowerLimit < smallestLocation:
            smallestLocation = subRange.lowerLimit
    
    return smallestLocation

print(part2())