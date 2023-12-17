import os
import sys
from enum import Enum

class CardinalDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Block():
    def __init__(self, coolingNumber, isEnd = False, visited = False) -> None:
        self.coolingNumber = coolingNumber
        self.isEnd = isEnd
        self.visited = visited
        self.minCooling = 0

memoTable = {}

def findLeastCoolingPath(grid, i, j, prevDirection, numSameDirection):
    global memoTable

    if grid[i][j].isEnd:
        return grid[i][j].coolingNumber
    
    if grid[i][j].visited:
        return float("inf")
    
    memKey = "row:{} column:{} {} {}".format(i, j, prevDirection.name, numSameDirection)
    if memKey in memoTable:
        return memoTable[memKey]

    grid[i][j].visited = True
    minCooling = float("inf")

    # Go North
    if (prevDirection == CardinalDirection.NORTH and numSameDirection == 3) == False and i > 0:
        newCooling = findLeastCoolingPath(grid, i-1, j, CardinalDirection.NORTH, numSameDirection+1 if prevDirection == CardinalDirection.NORTH else 1)
        minCooling = min(minCooling, newCooling)
    
    # Go West
    if (prevDirection == CardinalDirection.WEST and numSameDirection == 3) == False and j > 0:
        newCooling = findLeastCoolingPath(grid, i, j-1, CardinalDirection.WEST, numSameDirection+1 if prevDirection == CardinalDirection.WEST else 1)
        minCooling = min(minCooling, newCooling)
    
    # Go South
    if (prevDirection == CardinalDirection.SOUTH and numSameDirection == 3) == False and i < len(grid)-1:
        newCooling = findLeastCoolingPath(grid, i+1, j, CardinalDirection.SOUTH, numSameDirection+1 if prevDirection == CardinalDirection.SOUTH else 1)
        minCooling = min(minCooling, newCooling)
    

    # Go East
    if (prevDirection == CardinalDirection.EAST and numSameDirection == 3) == False and j < len(grid[0])-1:
        newCooling = findLeastCoolingPath(grid, i, j+1, CardinalDirection.EAST, numSameDirection+1 if prevDirection == CardinalDirection.EAST else 1)
        minCooling = min(minCooling, newCooling)
    
    grid[i][j].visited = False

    # Line below just for printing out what minCooling value is attached to each row
    grid[i][j].minCooling = minCooling

    if minCooling != float("inf"):
        memoTable[memKey] = minCooling + grid[i][j].coolingNumber
    return minCooling + grid[i][j].coolingNumber

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")
    grid = []

    for i, row in enumerate(rows):
        grid.append([])
        for num in row:
            grid[i].append(Block(int(num)))

    grid[len(grid)-1][len(grid[0])-1].isEnd = True

    sys.setrecursionlimit(100000)
    num = findLeastCoolingPath(grid,0,0,CardinalDirection.NORTH,0)

    for row in grid:
        for item in row:
            print("{:3}".format(item.minCooling), end=" ")
        print()
    return num - grid[0][0].coolingNumber

print(part1())

