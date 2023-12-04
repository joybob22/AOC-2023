import sys
import os
import re
import functools

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    
    pattern = r"^Card +\d+: +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? (\|) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)?$"
    cards = re.findall(pattern, contents, re.M)

    totalWinScore = 0
    for card in cards:
        winningNums = []
        checkIfWin = False
        cardWins = 0
        for item in card:
            if checkIfWin and item in winningNums:
                cardWins = 1 if cardWins == 0 else cardWins * 2
            elif item.isnumeric():
                winningNums.append(item)
            elif item == "|":
                checkIfWin = True
        totalWinScore += cardWins
    return totalWinScore

# print(part1())

def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    
    pattern = r"^Card +\d+: +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? (\|) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)? *(\d+)?$"
    cards = re.findall(pattern, contents, re.M)

    totalOfEachScratchCard = [1] * len(cards)
    for i, card in enumerate(cards):
        winningNums = []
        checkIfWin = False
        cardWins = 0
        for item in card:
            if checkIfWin and item in winningNums:
                cardWins += 1
            elif item.isnumeric():
                winningNums.append(item)
            elif item == "|":
                checkIfWin = True

        for k in range(totalOfEachScratchCard[i]):
            for j in range(cardWins):
                totalOfEachScratchCard[i+j+1]+=1

    return functools.reduce(lambda a, b: a+b, totalOfEachScratchCard)
print(part2())