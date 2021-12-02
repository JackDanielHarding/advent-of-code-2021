import itertools as it

with open("./input.txt", "r") as inputFile:
    readingsStr = inputFile.read().splitlines()
    readings = map(int, readingsStr)
    readingPairs = it.pairwise(readings)
    increasingPairs = map(lambda pair : pair[1] > pair[0], readingPairs)
    numOfIncreasingPairs = sum(increasingPairs)
    print (numOfIncreasingPairs)