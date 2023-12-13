import re
import os
import sys

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    patterns = contents.split("\n\n")
    
    horizontalNum = 0
    verticalNum = 0

    for pattern in patterns:
        pattern = pattern.split("\n")
        # First check horizontal
        foundHorizontalReflection = False
        
        for i in range(0, len(pattern)-1):
            pointerTop = i
            originalPointerTop = i
            pointerBottom = i+1
            foundReflection = True
            while pointerTop >= 0 and pointerBottom < len(pattern):
                if pattern[pointerTop] != pattern[pointerBottom]:
                    foundReflection = False
                    break
                pointerTop -= 1
                pointerBottom += 1
            if foundReflection:
                horizontalNum += (originalPointerTop+1)
                foundHorizontalReflection = True
                break
        
        if foundHorizontalReflection:
            continue

        # Now check for a vertical reflection
        for i in range(0, len(pattern[0])-1):
            pointerLeft = i
            originalPointerLeft = i
            pointerRight = i+1
            
            foundReflection = True
            while pointerLeft >= 0 and pointerRight < len(pattern[0]):
                isValid = True
                for j in range(0, len(pattern)):
                    if pattern[j][pointerLeft] != pattern[j][pointerRight]:
                        isValid = False
                        break
                if isValid == False:
                    foundReflection = False
                    break
                pointerLeft -= 1
                pointerRight += 1
            
            if foundReflection:
                verticalNum += (originalPointerLeft+1)
                break

    return verticalNum + (100 * horizontalNum)


# print(part1())

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    patterns = contents.split("\n\n")
    
    horizontalNum = 0
    verticalNum = 0

    for pattern in patterns:
        pattern = pattern.split("\n")
        foundHorizontalReflection = False
        foundVerticalReflection = False
        for changedi in range(0, len(pattern)):
            for changedj in range(0, len(pattern[0])):
                pattern[changedi] = pattern[changedi][:changedj] +  ("." if pattern[changedi][changedj] == "#" else "#") + pattern[changedi][changedj+1:]
                # for newRow in pattern:
                #     for item in newRow:
                #         print(item, end=" ")
                #     print()
                # First check horizontal
                
                for i in range(0, len(pattern)-1):
                    pointerTop = i
                    originalPointerTop = i
                    pointerBottom = i+1
                    foundReflection = True
                    while pointerTop >= 0 and pointerBottom < len(pattern):
                        if pattern[pointerTop] != pattern[pointerBottom]:
                            foundReflection = False
                            break
                        pointerTop -= 1
                        pointerBottom += 1
                        
                    if foundReflection and changedi >= (originalPointerTop - (len(pattern)-1 - (originalPointerTop+1))) and changedi - (originalPointerTop+1) <= originalPointerTop:
                        # for newRow in pattern:
                        #     for item in newRow:
                        #         print(item, end=" ")
                        #     print()
                        # print()
                        # print(str(originalPointerTop+1) + " " + str(changedi) + " " + str(len(pattern)-1) + " " + str((len(pattern)-1 - originalPointerTop+1)))
                        horizontalNum += (originalPointerTop+1)
                        foundHorizontalReflection = True
                        break
                
                if foundHorizontalReflection:
                    pattern[changedi] = pattern[changedi][:changedj] +  ("." if pattern[changedi][changedj] == "#" else "#") + pattern[changedi][changedj+1:]
                    break

                # Now check for a vertical reflection
                for i in range(0, len(pattern[0])-1):
                    pointerLeft = i
                    originalPointerLeft = i
                    pointerRight = i+1
                    
                    foundReflection = True
                    while pointerLeft >= 0 and pointerRight < len(pattern[0]):
                        isValid = True
                        for j in range(0, len(pattern)):
                            if pattern[j][pointerLeft] != pattern[j][pointerRight]:
                                isValid = False
                                break
                        if isValid == False:
                            foundReflection = False
                            break
                        pointerLeft -= 1
                        pointerRight += 1
                    
                    if foundReflection and changedj >= originalPointerLeft - (len(pattern[0])-1 - (originalPointerLeft+1)) and changedj - (originalPointerLeft+1) <= originalPointerLeft:
                        # print(changedj)
                        # print(originalPointerLeft)
                        # for newRow in pattern:
                        #     for item in newRow:
                        #         print(item, end=" ")
                        #     print()
                        verticalNum += (originalPointerLeft+1)
                        foundVerticalReflection = True
                        break
                pattern[changedi] = pattern[changedi][:changedj] +  ("." if pattern[changedi][changedj] == "#" else "#") + pattern[changedi][changedj+1:]
                if foundHorizontalReflection or foundVerticalReflection:
                    break
            if foundHorizontalReflection or foundVerticalReflection:
                break
    # print(verticalNum)
    # print(horizontalNum)
    return verticalNum + (100 * horizontalNum)

print(part2())
# someStr = "abc"
# print(someStr[:1] + "z" + someStr[2:])