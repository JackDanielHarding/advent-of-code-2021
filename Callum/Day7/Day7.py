from statistics import mean
from math import ceil, floor

with open("./input.txt", "r") as inputFile:
    positionsStrLine = inputFile.readline()
    
positionStrs = positionsStrLine.split(',')
positions = [int(positionStr) for positionStr in positionStrs]
positions.sort()
bestPosition = positions[((len(positions) + 1) // 2) - 1]

print(f'Best position basic: {sum(abs(position - bestPosition) for position in positions)}')

meanPosition = mean(positions)
bestPositionMin = floor(meanPosition)
fuelMinPosition = sum((abs(position - bestPositionMin) * (1 + abs(position - bestPositionMin)))//2  for position in positions)

bestPositionMax = ceil(meanPosition)
fuelMaxPosition = sum((abs(position - bestPositionMax) * (1 + abs(position - bestPositionMax)))//2  for position in positions)

print(f'Best position complex: {min(fuelMinPosition, fuelMaxPosition)}')