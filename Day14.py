import os
import sys

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")

    for j in range(0,len(rows[0])):
        for i in range(1,len(rows)):
            if rows[i][j] == "." or rows[i][j] == "#":
                continue
            pointer = i-1
            
            while pointer >= 0 and rows[pointer][j] == ".":
                pointer -= 1
            rows[i] = rows[i][:j] + "." + rows[i][j+1:]
            rows[pointer+1] = rows[pointer+1][:j] + "O" + rows[pointer+1][j+1:]
    
    totalWeight = 0
    for i, row in enumerate(rows):
        for char in row:
            if char == "O":
                totalWeight += len(rows) - i
    return totalWeight
# print(part1())



def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")

    
    dishToIndex = {}
    indexToDish = {}
    counter = 0
    startOfLoop = 0
    while counter < 1000000000:
        strRows = ""

        for row in rows:
            for char in row:
                strRows += char
            strRows += "\n"

        if strRows in dishToIndex:
            startOfLoop = dishToIndex[strRows]
            break

        dishToIndex[strRows] = counter
        indexToDish[counter] = strRows

        # North
        for j in range(0,len(rows[0])):
            for i in range(1,len(rows)):
                if rows[i][j] == "." or rows[i][j] == "#":
                    continue
                pointer = i-1
                
                while pointer >= 0 and rows[pointer][j] == ".":
                    pointer -= 1
                rows[i] = rows[i][:j] + "." + rows[i][j+1:]
                rows[pointer+1] = rows[pointer+1][:j] + "O" + rows[pointer+1][j+1:]
        
        # West
        for i in range(0, len(rows)):
            for j in range(1, len(rows[i])):
                if rows[i][j] == "." or rows[i][j] == "#":
                    continue
                pointer = j-1
                while pointer >= 0 and rows[i][pointer] == ".":
                    pointer -= 1
                rows[i] = rows[i][:j] + "." + rows[i][j+1:]
                rows[i] = rows[i][:pointer+1] + "O" + rows[i][pointer+2:]

        # South
        for j in range(0,len(rows[0])):
            for i in range(1,len(rows)):
                i = len(rows)-1-i
                if rows[i][j] == "." or rows[i][j] == "#":
                    continue
                pointer = i+1
                
                while pointer < len(rows) and rows[pointer][j] == ".":
                    pointer += 1
                rows[i] = rows[i][:j] + "." + rows[i][j+1:]
                rows[pointer-1] = rows[pointer-1][:j] + "O" + rows[pointer-1][j+1:]

        # East
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                j = len(rows[i]) - 1 - j
                if rows[i][j] == "." or rows[i][j] == "#":
                    continue
                pointer = j+1
                while pointer < len(rows[i]) and rows[i][pointer] == ".":
                    pointer += 1
                rows[i] = rows[i][:j] + "." + rows[i][j+1:]
                rows[i] = rows[i][:pointer-1] + "O" + rows[i][pointer:]
        counter += 1

    strRows = indexToDish[((1000000000 - startOfLoop) % (counter-(startOfLoop))) + startOfLoop]
    
    strRows = strRows.split("\n")
    totalWeight = 0
    for i, row in enumerate(strRows):
        for char in row:
            print(char, end="")
            if char == "O":
                totalWeight += len(rows) - i
        print()
    return totalWeight

print(part2())