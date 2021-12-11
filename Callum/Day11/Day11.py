import numpy as np

array = np.genfromtxt('./input.txt', delimiter=1, dtype=int)
flashed = np.zeros_like(array)

def flash(array, iy, ix):
    if not flashed[iy, ix]:
        flashed[iy, ix] = 1
        minY = max(iy-1, 0)
        maxY = min(iy+2, len(array))
        minX = max(ix-1, 0)
        maxX = min(ix+2, len(array[0]))
        arr = array[minY:maxY, minX:maxX]
        arr += 1
        for idy in range(minY, maxY):
            for idx in range(minX, maxX):
                val = array[idy, idx]
                if val > 9 and not flashed[idy, idx]:
                    flash(array, idy, idx)

flashSumStepNumber = 100
flashedSum = 0
allFlashedStep = -1
stepId = 1

while allFlashedStep == -1:
    flashed.fill(0)
    array += 1
    for iy, ix in np.ndindex(array.shape):
       val = array[iy, ix]
       if val > 9 and not flashed[iy, ix]:
           flash(array, iy, ix)
           
    stepFlashedSum = np.sum(flashed)
    flashedSum += stepFlashedSum
    
    for iy, ix in np.ndindex(array.shape):
        if flashed[iy, ix]:
            array[iy, ix] = 0
            
    if stepId == 100:
        print(f'Total flashes after {flashSumStepNumber} steps: {flashedSum}')
    
    if stepFlashedSum == flashed.size and allFlashedStep == -1:
        allFlashedStep = stepId
    
    stepId += 1

print(f'Step number where all Octopuses flashed {allFlashedStep}')