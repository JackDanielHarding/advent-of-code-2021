from Vent import Vent, AxisAlignedVent
from collections import Counter
from itertools import chain

with open("./input.txt", "r") as inputFile:
    ventStrs = inputFile.read().splitlines()
    
vents = [Vent(ventStr) for ventStr in ventStrs]

aaPoints = (vent.GetPoints() for vent in vents if isinstance(vent, AxisAlignedVent))
countedPoints = Counter(chain.from_iterable(aaPoints)).most_common()
atLeastTwoOverlappedPoints = (countedPoint for countedPoint in countedPoints if countedPoint[1] >= 2)
print(f'Number of overlapped vent axis aligned points: {len(list(atLeastTwoOverlappedPoints))}')

points = (vent.GetPoints() for vent in vents)
countedPoints = Counter(chain.from_iterable(points)).most_common()
atLeastTwoOverlappedPoints = (countedPoint for countedPoint in countedPoints if countedPoint[1] >= 2)
print(f'Number of overlapped vent points: {len(list(atLeastTwoOverlappedPoints))}')