import numpy as np
from scipy.signal import argrelmin

array = np.genfromtxt('./input.txt', delimiter=1, dtype=int)
array = np.pad(array, (1, 1), 'constant', constant_values=(10, 10))

minX = argrelmin(array, axis=1)
minY = argrelmin(array)

minXPoints = set()
for idx, minXPointsX in enumerate(minX[0]):
    minXPointsY = minX[1][idx]
    minXPoints.add((minXPointsX, minXPointsY))
    
minPoints = set()
for idx, minYPointsX in enumerate(minY[0]):
    minYPointsY = minY[1][idx]
    if (minYPointsX, minYPointsY) in minXPoints:
        minPoints.add((minYPointsX, minYPointsY))
        
        
def SearchFromPoint(point):
    if array[point[0]][point[1]] >= 9:
        return 0
    else:
        array[point[0]][point[1]] = 9
        return 1 + SearchFromPoint((point[0]-1, point[1]))+ SearchFromPoint((point[0]+1, point[1])) + SearchFromPoint((point[0], point[1]-1)) + SearchFromPoint((point[0], point[1]+1))

sum = 0
basinSizes = []
for minPoint in minPoints:
    sum += array[minPoint[0]][minPoint[1]] + 1
    sizeOfBasin = SearchFromPoint(minPoint)
    basinSizes.append(sizeOfBasin)
    
basinSizes.sort(reverse=True)

print(f'Sum of the risk levels: {sum}')
print(f'Product of the three largest basins: {basinSizes[0] * basinSizes[1] * basinSizes[2]}')
