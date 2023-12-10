import re
import os
import sys

class Position():
    def __init__(self, i, j, char) -> None:
        self.i = i
        self.j = j
        self.previousi = i
        self.previousj = j
        self.partOfLoop = False
        self.char = char
    
    def update(self, i, j):
        self.previousi = self.i
        self.previousj = self.j
        self.i = i
        self.j = j

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")

    # Find S
    sPosition = None
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            if item == "S":
                sPosition = Position(i,j)
                sPosition.partOfLoop = True
    
    # Determine two connecting pipes from S
    pipes = []
    if sPosition.i > 0 and (rows[sPosition.i-1][sPosition.j] == "|" or rows[sPosition.i-1][sPosition.j] == "7" or rows[sPosition.i-1][sPosition.j] == "F"):
        pipes.append(Position(sPosition.i-1, sPosition.j))
    if sPosition.i < len(rows)-1 and (rows[sPosition.i+1][sPosition.j] == "|" or rows[sPosition.i+1][sPosition.j] == "L" or rows[sPosition.i+1][sPosition.j] == "J"):
        pipes.append(Position(sPosition.i+1, sPosition.j))
    if sPosition.j > 0 and (rows[sPosition.i][sPosition.j-1] == "-" or rows[sPosition.i][sPosition.j-1] == "L" or rows[sPosition.i][sPosition.j-1] == "F"):
        pipes.append(Position(sPosition.i, sPosition.j-1))
    if sPosition.j < len(rows[0])-1 and (rows[sPosition.i][sPosition.j+1] == "-" or rows[sPosition.i][sPosition.j+1] == "J" or rows[sPosition.i][sPosition.j+1] == "7"):
        pipes.append(Position(sPosition.i, sPosition.j+1))

    # for pipe in pipes:
    #     print("i: " + str(pipe.i) + " j: " + str(pipe.j))

    numSteps = 1
    keepRunning = True
    while keepRunning:
        for pipe in pipes:
            char = rows[pipe.i][pipe.j]
            if char == "|":
                if pipe.previousi == pipe.i+1:
                    # We were just below this point so go up
                    pipe.update(pipe.i-1, pipe.j)
                else:
                    # We were just above this point so go down
                    pipe.update(pipe.i+1,pipe.j)
            if char == "-":
                if pipe.previousj == pipe.j-1:
                    # We were just left of this point so go right
                    pipe.update(pipe.i,pipe.j+1)
                else:
                    # We were just to the right of this point so go left
                    pipe.update(pipe.i,pipe.j-1)
            if char == "L":
                if pipe.previousi == pipe.i-1:
                    # We were just above this point to go right
                    pipe.update(pipe.i, pipe.j+1)
                else:
                    # We were just to the right of this point so go up
                    pipe.update(pipe.i-1,pipe.j)
            if char == "J":
                if pipe.previousi == pipe.i-1:
                    # We were just above this point so go left
                    pipe.update(pipe.i,pipe.j-1)
                else:
                    # We were just to the left so go up
                    pipe.update(pipe.i-1,pipe.j)
            if char == "7":
                if pipe.previousi == pipe.i+1:
                    # We were just below this point so go left
                    pipe.update(pipe.i,pipe.j-1)
                else:
                    # We were to the left so go down
                    pipe.update(pipe.i+1,pipe.j)
            if char == "F":
                if pipe.previousi == pipe.i+1:
                    # We were just below this point so go right
                    pipe.update(pipe.i,pipe.j+1)
                else:
                    # We were just to the right so go down
                    pipe.update(pipe.i+1,pipe.j)
        numSteps += 1
        if pipes[0].i == pipes[1].i and pipes[0].j == pipes[1].j:
            keepRunning = False

    return numSteps

    

# print(part1())

# This one was very tricky. Had to look up the conceptual idea of how to figure this out.
# The idea is that you can figure out if any point in the grid is inside or outside by doing the following:
# Take your point and assume it is outside the main pipe loop
# Look at all the points to the right and flip your assumption for the point being inside or outside the loop when you hit a piece of the main loop
# You have to be careful of counting parallel points of the pipe. So do not count "-", "L", or "J"
# After looking at all the points to the right of your original point in question you test your assumption. 
# If the assumption flipped to being inside then count it.

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")
    grid = []
    # Find S
    sPosition = None
    for i, row in enumerate(rows):
        grid.append([])
        for j, item in enumerate(row):
            if item == "S":
                sPosition = Position(i,j,item)
                grid[i].append(sPosition)
                sPosition.partOfLoop = True
            else:
                grid[i].append(Position(i,j,item))
    
    # Determine two connecting pipes from S
    pipes = []
    if sPosition.i > 0 and (rows[sPosition.i-1][sPosition.j] == "|" or rows[sPosition.i-1][sPosition.j] == "7" or rows[sPosition.i-1][sPosition.j] == "F"):
        pipes.append(grid[sPosition.i-1][sPosition.j])
    if sPosition.i < len(rows)-1 and (rows[sPosition.i+1][sPosition.j] == "|" or rows[sPosition.i+1][sPosition.j] == "L" or rows[sPosition.i+1][sPosition.j] == "J"):
        pipes.append(grid[sPosition.i+1][sPosition.j])
    if sPosition.j > 0 and (rows[sPosition.i][sPosition.j-1] == "-" or rows[sPosition.i][sPosition.j-1] == "L" or rows[sPosition.i][sPosition.j-1] == "F"):
        pipes.append(grid[sPosition.i][sPosition.j-1])
    if sPosition.j < len(rows[0])-1 and (rows[sPosition.i][sPosition.j+1] == "-" or rows[sPosition.i][sPosition.j+1] == "J" or rows[sPosition.i][sPosition.j+1] == "7"):
        pipes.append(grid[sPosition.i][sPosition.j+1])

    for pipe in pipes:
        pipe.partOfLoop = True
        # print("i: " + str(pipe.i) + " j: " + str(pipe.j))

    if pipes[0].j == sPosition.j and pipes[1].j == sPosition.j:
        # Both pipes are above and below sPosition
        sPosition.char = "|"
    elif pipes[0].i == sPosition.i and pipes[1].i == sPosition.i:
        # Both pipes are to the left and right of sPosition
        sPosition.char = "-"
    elif (pipes[0].i < sPosition.i and pipes[0].j == sPosition.j and pipes[1].j > sPosition.j and pipes[1].i == sPosition.i) or (pipes[1].i < sPosition.i and pipes[1].j == sPosition.j and pipes[0].j > sPosition.j and pipes[0].i == sPosition.i):
        sPosition.char = "L"
    elif (pipes[0].i < sPosition.i and pipes[0].j == sPosition.j and pipes[1].j < sPosition.j and pipes[1].i == sPosition.i) or (pipes[1].i < sPosition.i and pipes[1].j == sPosition.j and pipes[0].j < sPosition.j and pipes[0].i == sPosition.i):
        sPosition.char = "J"
    elif (pipes[0].i > sPosition.i and pipes[0].j == sPosition.j and pipes[1].i == sPosition.i and pipes[1].j < sPosition.j) or (pipes[0].i > sPosition.i and pipes[0].j == sPosition.j and pipes[1].i == sPosition.i and pipes[1].j < sPosition.j):
        sPosition.char = "7"
    else:
        sPosition.char = "F"

    # for row in grid:
    #     for item in row:
    #         print(item.char, end=" ")
    #     print()

    numSteps = 1
    keepRunning = True
    while keepRunning:
        for pipe in pipes:
            char = rows[pipe.i][pipe.j]
            if char == "|":
                if pipe.previousi == pipe.i+1:
                    # We were just below this point so go up
                    pipe.update(pipe.i-1, pipe.j)
                    grid[pipe.i][pipe.j].partOfLoop = True
                else:
                    # We were just above this point so go down
                    pipe.update(pipe.i+1,pipe.j)
                    grid[pipe.i][pipe.j].partOfLoop = True
            if char == "-":
                if pipe.previousj == pipe.j-1:
                    # We were just left of this point so go right
                    pipe.update(pipe.i,pipe.j+1)
                    grid[pipe.i][pipe.j].partOfLoop = True
                else:
                    # We were just to the right of this point so go left
                    pipe.update(pipe.i,pipe.j-1)
                    grid[pipe.i][pipe.j].partOfLoop = True
            if char == "L":
                if pipe.previousi == pipe.i-1:
                    # We were just above this point to go right
                    pipe.update(pipe.i, pipe.j+1)
                    grid[pipe.i][pipe.j].partOfLoop = True
                else:
                    # We were just to the right of this point so go up
                    pipe.update(pipe.i-1,pipe.j)
                    grid[pipe.i][pipe.j].partOfLoop = True
            if char == "J":
                if pipe.previousi == pipe.i-1:
                    # We were just above this point so go left
                    pipe.update(pipe.i,pipe.j-1)
                    grid[pipe.i][pipe.j].partOfLoop = True
                else:
                    # We were just to the left so go up
                    pipe.update(pipe.i-1,pipe.j)
                    grid[pipe.i][pipe.j].partOfLoop = True
            if char == "7":
                if pipe.previousi == pipe.i+1:
                    # We were just below this point so go left
                    pipe.update(pipe.i,pipe.j-1)
                    grid[pipe.i][pipe.j].partOfLoop = True
                else:
                    # We were to the left so go down
                    pipe.update(pipe.i+1,pipe.j)
                    grid[pipe.i][pipe.j].partOfLoop = True
            if char == "F":
                if pipe.previousi == pipe.i+1:
                    # We were just below this point so go right
                    pipe.update(pipe.i,pipe.j+1)
                    grid[pipe.i][pipe.j].partOfLoop = True
                else:
                    # We were just to the right so go down
                    pipe.update(pipe.i+1,pipe.j)
                    grid[pipe.i][pipe.j].partOfLoop = True
        numSteps += 1
        if pipes[0].i == pipes[1].i and pipes[0].j == pipes[1].j:
            keepRunning = False

    insideNum = 0
    for i, row in enumerate(grid):
        for k, position in enumerate(row):
            if position.partOfLoop == True:
                continue
            inside = False
            for j in range(position.j, len(row)):
                if row[j].partOfLoop and (row[j].char == "|" or row[j].char == "F" or row[j].char == "7"):
                    # print("Hit")
                    inside = not inside
            if inside == True:
                insideNum += 1
                # print(str(i) + " " + str(k))
                grid[i][k].char == "I"

    # for row in grid:
    #     for item in row:
    #         print(item.partOfLoop, end=" ")
    #     print()
                
    return insideNum

print(part2())