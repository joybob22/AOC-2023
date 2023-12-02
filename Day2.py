import re
import sys
import os

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()

    pattern = r"^Game (\d+): (.*)$"
    games = re.findall(pattern, contents, re.M)

    maxValues = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    addedGamedIDs = 0
    for gameID, gameData in games:
        pattern1 = r"(\d+) (blue|green|red)[,;]?"
        blocks = re.findall(pattern1, gameData)
        validGame = True
        for num, color in blocks:
            if int(num) > maxValues[color]:
                validGame = False
                break
        if validGame:
            addedGamedIDs += int(gameID)
    return addedGamedIDs


def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()

    pattern = r"^Game (\d+): (.*)$"
    games = re.findall(pattern, contents, re.M)

    minValues = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    addedGamedPowers = 0
    for gameID, gameData in games:
        pattern1 = r"(\d+) (blue|green|red)[,;]?"
        blocks = re.findall(pattern1, gameData)
        for num, color in blocks:
            if int(num) > minValues[color]:
                minValues[color] = int(num)
        addedGamedPowers += (minValues["blue"] * minValues["green"] * minValues["red"])
        minValues = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
    return addedGamedPowers

print(part2())