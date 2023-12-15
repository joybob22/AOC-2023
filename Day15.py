import os
import sys

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    items = contents.split(",")

    sumHashValues = 0

    for item in items:
        currentValue = 0
        for char in item:
            currentValue += ord(char)
            currentValue *= 17
            currentValue %= 256
        sumHashValues += currentValue
    
    return sumHashValues
# print(part1())

class Lense():
    def __init__(self, label, boxIndex, focalLength) -> None:
        self.label = label
        self.boxIndex = boxIndex
        self.focalLength = focalLength

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    items = contents.split(",")

    boxes = []
    for i in range(256):
        boxes.append([])

    for item in items:
        box = 0
        currentCharPosition = 0
        for i, char in enumerate(item):
            if char == "=" or char == "-":
                currentCharPosition = i
                break
            box += ord(char)
            box *= 17
            box %= 256
        if item[currentCharPosition] == "=":
            foundLabel = False
            for i, lense in enumerate(boxes[box]):
                if lense.label == item[:currentCharPosition]:
                    foundLabel = True
                    del boxes[box][i]
                    boxes[box].insert(i, Lense(item[:currentCharPosition],box,item[currentCharPosition+1]))
            if foundLabel == False:
                boxes[box].append(Lense(item[:currentCharPosition],box,item[currentCharPosition+1]))
        else:
            for i, lense in enumerate(boxes[box]):
                if lense.label == item[:currentCharPosition]:
                    del boxes[box][i]
                    break
    focusingPower = 0
    # for i, box in enumerate(boxes):
    #     print("Box " + str(i) + ": ")
    #     for lense in box:
    #         print("[" + lense.label + " " + lense.focalLength + "]", end=" ")
    #     print()
    for i, box in enumerate(boxes):
        for j, lense in enumerate(box):
            focusingPower += ((i+1) * (j+1) * int(lense.focalLength))
    
    return focusingPower
print(part2())
