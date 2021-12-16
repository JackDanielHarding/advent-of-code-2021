import numpy as np
from re import match

with open("./input.txt", "r") as inputFile:
    input = inputFile.read()

inputSplit = input.split("\n\n")
dotStrs = inputSplit[0].splitlines()
foldStrs = inputSplit[1].splitlines()

maxX = max(int(dot.split(',')[0]) for dot in dotStrs) + 1
maxY = max(int(dot.split(',')[1]) for dot in dotStrs) + 1

paper = np.zeros((maxY, maxX), bool)

for dotStr in dotStrs:
    dotSplit = dotStr.split(',')
    x = int(dotSplit[0])
    y = int(dotSplit[1])
    paper[y,x] = True
    
def foldArray(array, axis, index):
    if axis == 'y':
        preFoldedPart = array[index+1:]
        foldedPart = np.flip(preFoldedPart, axis=0)
        np.logical_or(array[index-len(foldedPart):index], foldedPart, array[index-len(foldedPart):index])
        return array[0:index]
    else:
        preFoldedPart = array[:,index+1:]
        foldedPart = np.flip(preFoldedPart, axis=1)
        np.logical_or(array[:,index-len(foldedPart[0]):index], foldedPart, array[:,index-len(foldedPart[0]):index])
        return array[:,0:index]

def fold(paper, foldStr):
    m = match('fold along ([x|y])=(\d+)', foldStr)
    if m:
        axis = m.group(1)
        index = int(m.group(2))
        
        return foldArray(paper, axis, index)
    else:
        raise ValueError

print(f'Number of dots after first fold: {np.sum(fold(paper, foldStrs[0]))}')

for foldStr in foldStrs:
    paper = fold(paper, foldStr)

np.set_printoptions(formatter={'bool':lambda x: '#' if x else ' '}, linewidth=100)
print("The code is:")
print(paper)