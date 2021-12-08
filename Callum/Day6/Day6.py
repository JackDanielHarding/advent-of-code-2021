from functools import lru_cache

@lru_cache
def NumberOfFishInFamilyZero(numberOfDays):
    if numberOfDays <= 0:
        return 1
    else:
        return NumberOfFishInFamilyZero(numberOfDays - 7) + NumberOfFishInFamilyZero(numberOfDays - 9)

with open("./input.txt", "r") as inputFile:
    countStrLine = inputFile.readline()

countStrs = countStrLine.split(',')
counts = [int(countStr) for countStr in countStrs]

print(f'Fish after 80 days: {sum(NumberOfFishInFamilyZero(80 - initialCount) for initialCount in counts)}')
print(f'Fish after 256 days: {sum(NumberOfFishInFamilyZero(256 - initialCount) for initialCount in counts)}')
