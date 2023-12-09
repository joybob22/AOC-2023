import re
import os
import sys

def part1():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r"^(-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)?$"
    sequences = re.findall(pattern, contents, re.M)

    # Clean up input mainly for sample input
    for i, sequence in enumerate(sequences):
        sequences[i] = list(sequence)
        for j, num in enumerate(sequences[i]):
            if num == "":
                sequences[i] = sequences[i][0:j]
                break
            sequences[i][j] = int(sequences[i][j])


    addedNewSequences = 0
    for sequence in sequences:
        patterns = [sequence]
        
        while listIsAllZeros(patterns[len(patterns) - 1]) == False:
            newSequence = []
            for i in range(0, len(patterns[len(patterns) - 1]) - 1):
                newSequence.append(patterns[len(patterns) - 1][i+1] - patterns[len(patterns) - 1][i])
            patterns.append(newSequence)
        for i in range(0, len(patterns) - 1):
            index = len(patterns) - 1 - i
            patterns[index - 1].append(patterns[index][len(patterns[index])-1] + patterns[index - 1][len(patterns[index - 1])-1])
        addedNewSequences += patterns[0][len(patterns[0])-1]
    return addedNewSequences

def listIsAllZeros(nums):
    isAllZeros = True
    for num in nums:
        if int(num) != 0:
            isAllZeros = False
            break
    return isAllZeros

# print(part1())


def part2():
    inputFileName = sys.argv[1]
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "./inputFiles/" + inputFileName), "r") as f:
        contents = f.read()
    pattern = r"^(-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)? ?(-?\d+)?$"
    sequences = re.findall(pattern, contents, re.M)

    # Clean up input mainly for sample input
    for i, sequence in enumerate(sequences):
        sequences[i] = list(sequence)
        for j, num in enumerate(sequences[i]):
            if num == "":
                sequences[i] = sequences[i][0:j]
                break
            sequences[i][j] = int(sequences[i][j])


    addedNewSequences = 0
    for sequence in sequences:
        patterns = [sequence]
        
        while listIsAllZeros(patterns[len(patterns) - 1]) == False:
            newSequence = []
            for i in range(0, len(patterns[len(patterns) - 1]) - 1):
                newSequence.append(patterns[len(patterns) - 1][i+1] - patterns[len(patterns) - 1][i])
            patterns.append(newSequence)
        for i in range(0, len(patterns) - 1):
            index = len(patterns) - 1 - i
            patterns[index - 1].insert(0, patterns[index - 1][0] - patterns[index][0])
        addedNewSequences += patterns[0][0]
    return addedNewSequences

print(part2())