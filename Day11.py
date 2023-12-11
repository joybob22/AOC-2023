import os
import sys

class Point():
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
        self.expansionValuei = 0
        self.expansionValuej = 0
        self.char = "."

    def expandiValue(self):
        self.expansionValuei += 999999
    
    def expandjValue(self):
        self.expansionValuej += 999999

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")

    # Determine if an entire row is just empty space
    createdSpace = False
    for i, row in enumerate(rows):
        if createdSpace:
            createdSpace = False
            continue
        isEmptyRow = True
        for char in row:
            if char == "#":
                isEmptyRow = False
                break
        if isEmptyRow:
            rows.insert(i,"." * len(rows[i]))
            createdSpace = True
    
    # Determine if an entire column is just empty space
    createdSpace = False
    j = 0
    while j < len(rows[0]):
        if createdSpace:
            createdSpace = False
            j += 1
            continue
        isEmptyColumn = True
        for i in range(0,len(rows)):
            if rows[i][j] == "#":
                isEmptyColumn = False
                break
        if isEmptyColumn:
            for i in range(0,len(rows)):
                rows[i] = rows[i][:j] + "." + rows[i][j:]
            createdSpace = True
        j += 1

    # for row in rows:
    #     for char in row:
    #         print(char, end=" ")
    #     print()

    galaxies = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "#":
                galaxies.append(Point(i,j))
    
    numSteps = 0
    for galaxy in galaxies:
        for galaxyTwo in galaxies:
            if galaxy.i == galaxyTwo.i and galaxy.j == galaxyTwo.j:
                continue
            numSteps += abs(galaxyTwo.i - galaxy.i) + abs(galaxyTwo.j - galaxy.j)
    return numSteps / 2
# print(part1())

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")
    grid = []
    # Determine if an entire row is just empty space

    for i, row in enumerate(rows):
        grid.append([])
        isEmptyRow = True
        for j, char in enumerate(row):
            item = Point(i,j)
            if char == "#":
                isEmptyRow = False
                item.char = "#"
            grid[i].append(item)
        if isEmptyRow:
            for point in grid[i]:
                point.expandiValue()
    
    # Determine if an entire column is just empty space
    j = 0
    while j < len(rows[0]):
        isEmptyColumn = True
        for i in range(0,len(rows)):
            if rows[i][j] == "#":
                isEmptyColumn = False
                break
        if isEmptyColumn:
            for i in range(0,len(rows)):
                grid[i][j].expandjValue()
        j += 1

    # for row in rows:
    #     for char in row:
    #         print(char, end=" ")
    #     print()

    galaxies = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "#":
                galaxies.append(grid[i][j])
    
    numSteps = 0
    for galaxy in galaxies:
        for galaxyTwo in galaxies:
            if galaxy.i == galaxyTwo.i and galaxy.j == galaxyTwo.j:
                continue
            totalExpandedValuei = 0
            for numRows in range(0, abs(galaxyTwo.i - galaxy.i)):
                if galaxyTwo.i - galaxy.i < 0:
                    totalExpandedValuei += grid[galaxy.i-numRows][galaxy.j].expansionValuei
                else:
                    totalExpandedValuei += grid[galaxyTwo.i-numRows][galaxyTwo.j].expansionValuei
            totalExpandedValuej = 0
            for columnNum in range(0, abs(galaxyTwo.j - galaxy.j)):
                if galaxyTwo.j - galaxy.j < 0:
                    totalExpandedValuej += grid[galaxy.i][galaxy.j-columnNum].expansionValuej
                else:
                    totalExpandedValuej += grid[galaxyTwo.i][galaxyTwo.j-columnNum].expansionValuej
            numSteps += totalExpandedValuei
            numSteps += totalExpandedValuej
            numSteps += abs(galaxyTwo.i - galaxy.i) + abs(galaxyTwo.j - galaxy.j)
            print("From: " + str(galaxy.i) + ", " + str(galaxy.j) + " To: " + str(galaxyTwo.i) + ", " + str(galaxyTwo.j) + " Distance: " + str(abs(galaxyTwo.i - galaxy.i) + abs(galaxyTwo.j - galaxy.j)) + " Expandi: " + str(totalExpandedValuei) + " Expandj: " + str(totalExpandedValuej))
    return numSteps / 2
print(part2())