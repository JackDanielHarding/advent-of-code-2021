from functools import reduce
from re import finditer, subn
from typing import Match
from itertools import combinations

with open("./input.txt", "r") as inputFile:
    numbersStr = inputFile.read().splitlines()
    
def trySplit(number: str) -> tuple[bool, str]:
    twoDigitNumbers = [(m.group(),m.start(),m.end()) for m in finditer(r'(\d{2,})', number)]
    if any(twoDigitNumbers):
        (nextNumberStr, start, end) = twoDigitNumbers[0]
        nextNumber = int(nextNumberStr)
        left = nextNumber // 2
        right = (nextNumber + 1) // 2
        number = ''.join([number[:start],f'[{left},{right}]',number[end:]])
        return True, number
    return False, number
    
def tryExplode(number: str) -> tuple[bool, str]:
    nested = 0
    for index, char in enumerate(number):
        if char == '[':
            nested += 1
        if char == ']':
            nested -= 1
        
        if nested == 5:
            commaIndex = number.find(',', index + 2)
            endIndex = number.find(']', commaIndex + 2)
            left = int(number[index + 1:commaIndex])
            right = int(number[commaIndex + 1:endIndex])
            
            rightNumMatches = [(m.group(),m.start(),m.end()) for m in finditer(r'(\d+)', number[endIndex+2:])]
            if any(rightNumMatches):
                (nextRightNumber, rStart, rEnd) = rightNumMatches[0]
                newRight = str(right + int(nextRightNumber))
                number = ''.join([number[:endIndex + 2 + rStart],newRight,number[endIndex + 2 + rEnd:]])
                
            number = ''.join([number[:index], '0', number[endIndex+1:]])
            
            leftNumMatches = [(m.group(),m.start(),m.end()) for m in finditer(r'(\d+)', number[:index-1])]
            if any(leftNumMatches):
                (nextLeftNumber, lStart, lEnd) = leftNumMatches[-1]
                newLeft = str(left + int(nextLeftNumber))
                number = ''.join([number[:lStart],newLeft,number[lEnd:]])
            
            return True, number
        
    return False, number

def add(left: str, right: str) -> str:
    sum = f'[{left},{right}]'
    modified = True
    while modified:
        modified, sum = tryExplode(sum)
        if not modified:
            modified, sum = trySplit(sum)
    return sum

def subWithMagnitude(match : Match) -> str:
    return str(3 * int(match.group(1)) + 2 * int(match.group(2)))

def getMagnitude(number: str) -> int:
    while True:
        (number, subs) = subn(r'\[(\d+),(\d+)\]', subWithMagnitude, number)
        if subs == 0:
            break
    return int(number)
    
finalNumber = reduce(lambda sum, next: add(sum, next), numbersStr)
print(f'Magnitude of final sum: {getMagnitude(finalNumber)}')

sumPairs = list(combinations(numbersStr, 2))
maxSum = 0
for (left, right) in sumPairs:
    aSum = getMagnitude(add(left, right))
    bSum = getMagnitude(add(right, left))
    maxSum = max(maxSum, max(aSum, bSum))
    
print(f'Largest magnitude of any sum of two different numbers: {maxSum}')