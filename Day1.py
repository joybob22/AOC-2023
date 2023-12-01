import sys
import os

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    contents = contents.split("\n")

    sumOfCalibrationValues = 0
    for line in contents:
        nums = []
        for char in line:
            if char.isnumeric():
                nums.append(char)
        sumOfCalibrationValues += int(nums[0] + nums[len(nums)-1])
    return sumOfCalibrationValues
    

# print(part1())

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    contents = contents.split("\n")

    sumOfCalibrationValues = 0
    for line in contents:
        nums = []
        potentialNum = ""
        for char in line:
            potentialNum += char
            if char.isnumeric():
                nums.append(char)
            checkedNum = checkForSpelledOutNum(potentialNum)
            if checkedNum:
                nums.append(checkedNum)
        sumOfCalibrationValues += int(nums[0] + nums[len(nums)-1])
    return sumOfCalibrationValues

def checkForSpelledOutNum(str):
    str = str.lower()

    if len(str) > 2:
        endOfStr = str[len(str)-3:len(str)]
        if endOfStr == "one":
            return "1"
        elif endOfStr == "two":
            return "2"
        elif endOfStr == "six":
            return "6"
    if len(str) > 3:
        endOfStr = str[len(str)-4:len(str)]
        if endOfStr == "four":
            return "4"
        elif endOfStr == "five":
            return "5"
        elif endOfStr == "nine":
            return "9"
    if len(str) > 4:
        endOfStr = str[len(str)-5:len(str)]
        if endOfStr == "three":
            return "3"
        elif endOfStr == "seven":
            return "7"
        elif endOfStr == "eight":
            return "8"
    return None

print(part2())