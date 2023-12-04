import re
import sys
import os

class GridItem():
    def __init__(self, char, visited = False) -> None:
        self.char = char
        self.visited = visited

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")
    grid = []
    
    for i, row in enumerate(rows):
        grid.append([])
        for j, char in enumerate(row):
            grid[i].append(GridItem(char))
    
    sumOfPartNumbers = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item.char.isnumeric() == False and item.char != ".":
                # We found a symbol
                if i > 0 and j > 0 and grid[i-1][j-1].char.isnumeric():
                    # Look top left
                    sumOfPartNumbers += constructNum(grid, i-1, j-1)
                if j > 0 and grid[i][j-1].char.isnumeric():
                    # Look left
                    sumOfPartNumbers += constructNum(grid, i, j-1)
                if i > 0 and grid[i-1][j].char.isnumeric():
                    # Look up
                    sumOfPartNumbers += constructNum(grid, i-1, j)
                if i > 0 and j < len(grid[i])-1 and grid[i-1][j+1].char.isnumeric():
                    # Look top right
                    sumOfPartNumbers += constructNum(grid, i-1, j+1)
                if j < len(grid[i])-1 and grid[i][j+1].char.isnumeric():
                    # Look right
                    sumOfPartNumbers += constructNum(grid, i, j+1)
                if i < len(grid)-1 and j < len(grid[i])-1 and grid[i+1][j+1].char.isnumeric():
                    # Look bottom right
                    sumOfPartNumbers += constructNum(grid, i+1, j+1)
                if i < len(grid)-1 and grid[i+1][j].char.isnumeric():
                    # Look down
                    sumOfPartNumbers += constructNum(grid, i+1, j)
                if i < len(grid)-1 and j > 0 and grid[i+1][j-1].char.isnumeric():
                    # Look bottom left
                    sumOfPartNumbers += constructNum(grid, i+1, j-1)
    
    return sumOfPartNumbers

def constructNum(g, i, j):
    if g[i][j].visited:
        return 0
    
    finalNum = [g[i][j].char]
    g[i][j].visited = True
    keepSearchingLeft = True
    keepSearchingRight = True
    row = i
    column = j

    while keepSearchingLeft:
        column -= 1
        if column < 0 or g[row][column].char.isnumeric() == False:
            keepSearchingLeft = False
            break
        
        finalNum.insert(0,g[row][column].char)
        g[row][column].visited = True
    
    row = i
    column = j

    while keepSearchingRight:
        column += 1
        if column > len(g[row])-1 or g[row][column].char.isnumeric() == False:
            keepSearchingRight = False
            break
        
        finalNum.append(g[row][column].char)
        g[row][column].visited = True

    finalNum = "".join(finalNum)
    return int(finalNum)

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")
    grid = []
    
    for i, row in enumerate(rows):
        grid.append([])
        for j, char in enumerate(row):
            grid[i].append(GridItem(char))
    
    sumOfGearRatios = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item.char == "*":
                # We found a potential gear
                gearRatio = 0
                amountOfParts = 0
                if i > 0 and j > 0 and grid[i-1][j-1].char.isnumeric():
                    # Look top left
                    partNumber = constructNum(grid, i-1, j-1)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if j > 0 and grid[i][j-1].char.isnumeric():
                    # Look left
                    partNumber = constructNum(grid, i, j-1)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if i > 0 and grid[i-1][j].char.isnumeric():
                    # Look up
                    partNumber = constructNum(grid, i-1, j)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if i > 0 and j < len(grid[i])-1 and grid[i-1][j+1].char.isnumeric():
                    # Look top right
                    partNumber = constructNum(grid, i-1, j+1)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if j < len(grid[i])-1 and grid[i][j+1].char.isnumeric():
                    # Look right
                    partNumber = constructNum(grid, i, j+1)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if i < len(grid)-1 and j < len(grid[i])-1 and grid[i+1][j+1].char.isnumeric():
                    # Look bottom right
                    partNumber = constructNum(grid, i+1, j+1)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if i < len(grid)-1 and grid[i+1][j].char.isnumeric():
                    # Look down
                    partNumber = constructNum(grid, i+1, j)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                if i < len(grid)-1 and j > 0 and grid[i+1][j-1].char.isnumeric():
                    # Look bottom left
                    partNumber = constructNum(grid, i+1, j-1)
                    if amountOfParts > 0 and partNumber > 0:
                        gearRatio *= partNumber
                        amountOfParts += 1
                    elif partNumber > 0:
                        gearRatio += partNumber
                        amountOfParts += 1
                # Check to be sure we have a valid gear
                if amountOfParts == 2:
                    sumOfGearRatios += gearRatio
    
    return sumOfGearRatios

print(part2())