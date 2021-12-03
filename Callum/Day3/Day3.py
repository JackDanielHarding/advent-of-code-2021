from collections import Counter
from functools import reduce

with open("./input.txt", "r") as inputFile:
    readingsStr = inputFile.read().splitlines()

columnsRange = range(len(readingsStr[0]))
columns = map(lambda columnIndex : map(lambda row : row[columnIndex], readingsStr), columnsRange)
multiModes = map(lambda column: Counter(column).most_common(), columns)
multiModesWithoutCount = map(lambda mm: (mm[0][0], mm[1][0]), multiModes)
rates = reduce(lambda multiModeX, multiModeY: [multiModeX[0] + multiModeY[0], multiModeX[1] + multiModeY[1]], multiModesWithoutCount)
gamma = int(rates[0], 2)
epsilon = int(rates[1], 2)
print(f'Gamma: {gamma}, Epsilon: {epsilon}, Power: {gamma * epsilon}')

# Part 2

oxygenFilteredReadings = readingsStr.copy()
co2FilteredReadings = readingsStr.copy()

for columnIndex in range(len(readingsStr[0])):
    oxygenColumns = map(lambda row : row[columnIndex], oxygenFilteredReadings)
    oxygenCounter = Counter(oxygenColumns)
    oxygenMostCommon = oxygenCounter.most_common()[0]
    oxygenMostCommonVal = oxygenMostCommon[0]
    if oxygenMostCommon[1] == oxygenCounter.total() / 2:
        oxygenMostCommonVal = '1'
    oxygenFilteredReadings = list(filter(lambda row : row[columnIndex] == oxygenMostCommonVal, oxygenFilteredReadings))

    co2Columns = map(lambda row : row[columnIndex], co2FilteredReadings)
    co2Counter = Counter(co2Columns)
    co2MostCommon = co2Counter.most_common()
    co2LeastCommon = co2MostCommon[len(co2MostCommon)-1]
    co2LeastCommonVal = co2LeastCommon[0]
    if co2LeastCommon[1] == co2Counter.total() / 2:
        co2LeastCommonVal = '0'
    co2FilteredReadings = list(filter(lambda row : row[columnIndex] == co2LeastCommonVal, co2FilteredReadings))
    
oxygen = int(oxygenFilteredReadings[0], 2)
co2 = int(co2FilteredReadings[0], 2)
print(f'Oxygen: {oxygen}, CO2: {co2}, Life Support Rating: {oxygen * co2}')