import os
import sys
from enum import Enum

class CardinalDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Tile():
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.energized = False
        self.previousDirections = []

class Beam():
    def __init__(self, i, j, currentDirection) -> None:
        self.i = i
        self.j = j
        self.currentDirection = currentDirection

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")

    # Setup Grid
    grid = []

    for i, row in enumerate(rows):
        grid.append([])
        for char in row:
            grid[i].append(Tile(char))
    
    startingBeam = Beam(0,0,CardinalDirection.EAST)
    beams = [startingBeam]
    grid[0][0].energized = True
    if grid[0][0].symbol != ".":
        if grid[0][0].symbol == "\\":
            startingBeam.currentDirection = CardinalDirection.SOUTH
        elif grid[0][0].symbol == "/":
            startingBeam.currentDirection = CardinalDirection.NORTH
        elif grid[0][0].symbol == "|":
            startingBeam.currentDirection = CardinalDirection.SOUTH

    while len(beams) > 0:
        beam = beams[0]
        newi = beam.i
        newj = beam.j

        if beam.currentDirection == CardinalDirection.NORTH:
            newi -= 1
        elif beam.currentDirection == CardinalDirection.EAST:
            newj += 1
        elif beam.currentDirection == CardinalDirection.SOUTH:
            newi += 1
        elif beam.currentDirection == CardinalDirection.WEST:
            newj -= 1
        
        # All of the cases to stop using this beam
        if newi < 0 or newi >= len(grid) or newj < 0 or newj >= len(grid[0]) or beam.currentDirection in grid[newi][newj].previousDirections:
            beams.pop(0)
            continue

        grid[newi][newj].energized = True
        beam.i = newi
        beam.j = newj
        grid[newi][newj].previousDirections.append(beam.currentDirection)

        if grid[newi][newj].symbol == ".":
            continue
        if grid[newi][newj].symbol == "\\":
            if beam.currentDirection == CardinalDirection.NORTH:
                beam.currentDirection = CardinalDirection.WEST
            elif beam.currentDirection == CardinalDirection.EAST:
                beam.currentDirection = CardinalDirection.SOUTH
            elif beam.currentDirection == CardinalDirection.SOUTH:
                beam.currentDirection = CardinalDirection.EAST
            elif beam.currentDirection == CardinalDirection.WEST:
                beam.currentDirection = CardinalDirection.NORTH
            continue
        if grid[newi][newj].symbol == "/":
            if beam.currentDirection == CardinalDirection.NORTH:
                beam.currentDirection = CardinalDirection.EAST
            elif beam.currentDirection == CardinalDirection.EAST:
                beam.currentDirection = CardinalDirection.NORTH
            elif beam.currentDirection == CardinalDirection.SOUTH:
                beam.currentDirection = CardinalDirection.WEST
            elif beam.currentDirection == CardinalDirection.WEST:
                beam.currentDirection = CardinalDirection.SOUTH
            continue
        if grid[newi][newj].symbol == "|":
            if beam.currentDirection == CardinalDirection.SOUTH or beam.currentDirection == CardinalDirection.NORTH:
                continue
            beam.currentDirection = CardinalDirection.NORTH
            beams.append(Beam(newi,newj,CardinalDirection.SOUTH))
            continue
        if grid[newi][newj].symbol == "-":
            if beam.currentDirection == CardinalDirection.EAST or beam.currentDirection == CardinalDirection.WEST:
                continue
            beam.currentDirection = CardinalDirection.EAST
            beams.append(Beam(newi, newj, CardinalDirection.WEST))

    energizedTiles = 0
    for row in grid:
        for tile in row:
            if tile.energized:
                energizedTiles += 1
    
    return energizedTiles

# print(part1())


def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    rows = contents.split("\n")

    # Setup Grid
    grid = []

    for i, row in enumerate(rows):
        grid.append([])
        for char in row:
            grid[i].append(Tile(char))
    
    startingBeams = []

    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if i == 0:
                startingBeams.append(Beam(i,j,CardinalDirection.SOUTH))
            if j == 0:
                startingBeams.append(Beam(i,j,CardinalDirection.EAST))
            if i == len(grid)-1:
                startingBeams.append(Beam(i,j,CardinalDirection.NORTH))
            if j == len(row)-1:
                startingBeams.append(Beam(i,j,CardinalDirection.WEST))

    mostEnergizedTiles = 0
    for startingBeam in startingBeams:
        beams = [startingBeam]
        grid[startingBeam.i][startingBeam.j].energized = True

        # This is ugly...I should have just changed the order inside my while loop...but laziness prevails
        if grid[startingBeam.i][startingBeam.j].symbol == "\\":
            if startingBeam.currentDirection == CardinalDirection.NORTH:
                startingBeam.currentDirection = CardinalDirection.WEST
            elif startingBeam.currentDirection == CardinalDirection.EAST:
                startingBeam.currentDirection = CardinalDirection.SOUTH
            elif startingBeam.currentDirection == CardinalDirection.SOUTH:
                startingBeam.currentDirection = CardinalDirection.EAST
            elif startingBeam.currentDirection == CardinalDirection.WEST:
                startingBeam.currentDirection = CardinalDirection.NORTH
        if grid[startingBeam.i][startingBeam.j].symbol == "/":
            if startingBeam.currentDirection == CardinalDirection.NORTH:
                startingBeam.currentDirection = CardinalDirection.EAST
            elif startingBeam.currentDirection == CardinalDirection.EAST:
                startingBeam.currentDirection = CardinalDirection.NORTH
            elif startingBeam.currentDirection == CardinalDirection.SOUTH:
                startingBeam.currentDirection = CardinalDirection.WEST
            elif startingBeam.currentDirection == CardinalDirection.WEST:
                startingBeam.currentDirection = CardinalDirection.SOUTH
        if grid[startingBeam.i][startingBeam.j].symbol == "|":
            if startingBeam.currentDirection != CardinalDirection.SOUTH and startingBeam.currentDirection != CardinalDirection.NORTH:
                startingBeam.currentDirection = CardinalDirection.NORTH
                beams.append(Beam(startingBeam.i,startingBeam.j,CardinalDirection.SOUTH))
        if grid[startingBeam.i][startingBeam.j].symbol == "-":
            if startingBeam.currentDirection != CardinalDirection.EAST and startingBeam.currentDirection != CardinalDirection.WEST:
                startingBeam.currentDirection = CardinalDirection.EAST
                beams.append(Beam(startingBeam.i, startingBeam.j, CardinalDirection.WEST))

        while len(beams) > 0:
            beam = beams[0]
            newi = beam.i
            newj = beam.j

            if beam.currentDirection == CardinalDirection.NORTH:
                newi -= 1
            elif beam.currentDirection == CardinalDirection.EAST:
                newj += 1
            elif beam.currentDirection == CardinalDirection.SOUTH:
                newi += 1
            elif beam.currentDirection == CardinalDirection.WEST:
                newj -= 1
            
            # All of the cases to stop using this beam
            if newi < 0 or newi >= len(grid) or newj < 0 or newj >= len(grid[0]) or beam.currentDirection in grid[newi][newj].previousDirections:
                beams.pop(0)
                continue

            grid[newi][newj].energized = True
            beam.i = newi
            beam.j = newj
            grid[newi][newj].previousDirections.append(beam.currentDirection)

            if grid[newi][newj].symbol == ".":
                continue
            if grid[newi][newj].symbol == "\\":
                if beam.currentDirection == CardinalDirection.NORTH:
                    beam.currentDirection = CardinalDirection.WEST
                elif beam.currentDirection == CardinalDirection.EAST:
                    beam.currentDirection = CardinalDirection.SOUTH
                elif beam.currentDirection == CardinalDirection.SOUTH:
                    beam.currentDirection = CardinalDirection.EAST
                elif beam.currentDirection == CardinalDirection.WEST:
                    beam.currentDirection = CardinalDirection.NORTH
                continue
            if grid[newi][newj].symbol == "/":
                if beam.currentDirection == CardinalDirection.NORTH:
                    beam.currentDirection = CardinalDirection.EAST
                elif beam.currentDirection == CardinalDirection.EAST:
                    beam.currentDirection = CardinalDirection.NORTH
                elif beam.currentDirection == CardinalDirection.SOUTH:
                    beam.currentDirection = CardinalDirection.WEST
                elif beam.currentDirection == CardinalDirection.WEST:
                    beam.currentDirection = CardinalDirection.SOUTH
                continue
            if grid[newi][newj].symbol == "|":
                if beam.currentDirection == CardinalDirection.SOUTH or beam.currentDirection == CardinalDirection.NORTH:
                    continue
                beam.currentDirection = CardinalDirection.NORTH
                beams.append(Beam(newi,newj,CardinalDirection.SOUTH))
                continue
            if grid[newi][newj].symbol == "-":
                if beam.currentDirection == CardinalDirection.EAST or beam.currentDirection == CardinalDirection.WEST:
                    continue
                beam.currentDirection = CardinalDirection.EAST
                beams.append(Beam(newi, newj, CardinalDirection.WEST))

        energizedTiles = 0
        for row in grid:
            for tile in row:
                if tile.energized:
                    energizedTiles += 1

        if energizedTiles > mostEnergizedTiles:
            mostEnergizedTiles = energizedTiles

        # reset grid
        for row in grid:
            for tile in row:
                tile.previousDirections = []
                tile.energized = False

    return mostEnergizedTiles

print(part2())