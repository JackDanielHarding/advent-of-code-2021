with open("./input.txt", "r") as inputFile:
    inputStrs = inputFile.read().splitlines()
    
    
uniqueOutputCount = 0
for inputStr in inputStrs:
    inputSectioned = inputStr.split('|')
    for output in inputSectioned[1].split(' '):
        if(len(output) in (2, 3, 4, 7)):
            uniqueOutputCount += 1
            
print(uniqueOutputCount)