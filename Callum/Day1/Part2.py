import itertools as it

with open("./input.txt", "r") as inputFile:
    readingsStr = inputFile.read().splitlines()
    readings = map(int, readingsStr)
    readingA, readingB, readingC = it.tee(readings, 3)
    next(readingB, None)
    next(readingC, None)
    next(readingC, None)
    readingTrips = zip(readingA, readingB, readingC)
    averageThreeReadings = map(lambda trip: trip[0] + trip[1] + trip[2], readingTrips)
    averagePairs = it.pairwise(averageThreeReadings)
    increasingPairs = map(lambda pair : pair[1] > pair[0], averagePairs)
    numOfIncreasingPairs = sum(increasingPairs)
    print (numOfIncreasingPairs)