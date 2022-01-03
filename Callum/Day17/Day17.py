from re import match
from numpy import ceil, sqrt

with open("./input.txt", "r") as inputFile:
    input = inputFile.read()
    
m = match('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', input)
xMin, xMax = (int(m.group(1)), int(m.group(2)))
yMin, yMax = (int(m.group(3)), int(m.group(4)))

yBest = abs(yMin) - 1
highestYPos = (yBest * (yBest + 1)) // 2
print(f'The highest Y position is {highestYPos}, resulting from an initial speed of {yBest}')

xInitialMin = int(ceil((sqrt(8 * xMin + 1) - 1)/2))
maxT = abs(yMin * 2)

def GetXPositions(x):
    xPositions = []
    pos = 0
    t = 0
    while True:
        xPositions.append((pos, t))
        pos += x
        if x > 0:
            x = x - 1
        elif x < 0:
            x = x + 1
        t += 1
        if x == 0 and t > maxT:
            break
        if pos > xMax:
            break
    return xPositions

def GetYPositions(y):
    yPositions = []
    pos = 0
    t = 0
    while True:
        yPositions.append((pos, t))
        pos += y
        y = y - 1
        t += 1
        if pos < yMin:
            break
    return yPositions

validInitialXs = dict()
for x in range(xInitialMin, xMax+1):
    for pos in GetXPositions(x):
        if pos[0] >= xMin and pos[0] <= xMax:
            if x not in validInitialXs:
                validInitialXs[x] = list()
            validInitialXs[x].append(pos[1])
            
validInitialYs = dict()
for y in range(yMin, yBest+1):
    for pos in GetYPositions(y):
        if pos[0] >= yMin and pos[0] <= yMax:
            if y not in validInitialYs:
                validInitialYs[y] = list()
            validInitialYs[y].append(pos[1])
                               
countValidDistinct = 0        
for (x, ts) in validInitialXs.items():
    countValidDistinct += len([y for y in validInitialYs.items() if any(t in ts for t in y[1])])
    
print(f'Number of distinct velocities that end up in target at any step: {countValidDistinct}')