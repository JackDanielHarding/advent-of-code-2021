from collections import Counter

with open("./input.txt", "r") as inputFile:
    inputStrs = inputFile.read().splitlines()
    
    
outputSum = 0
for inputStr in inputStrs:
    inputSplit = inputStr.split('|')
    digits = inputSplit[0].split(' ')
    
    seven = [digit for digit in digits if len(digit) == 3][0]
    one = [digit for digit in digits if len(digit) == 2][0]
    
    top = [char for char in seven if char not in one][0]
    
    chars = [char for digit in digits for char in digit]
    charCounter = Counter(chars).most_common()
    
    charCounter.remove((top, 8))
    
    botLeft = [charWithCount[0] for charWithCount in charCounter if charWithCount[1] == 4][0]
    topLeft = [charWithCount[0] for charWithCount in charCounter if charWithCount[1] == 6][0]
    topRight = [charWithCount[0] for charWithCount in charCounter if charWithCount[1] == 8][0]
    
    output = inputSplit[1].split(' ')
    
    outputNumber = 0
    outputTens = 1000
    
    for outputDigit in output:
        if outputDigit:
            outputDigitChars = [char for char in outputDigit]
            
            digitVal = 0
            
            match len(outputDigitChars):
                case 2:
                    digitVal = 1
                case 3:
                    digitVal = 7
                case 4:
                    digitVal = 4
                case 7:
                    digitVal = 8
                case 5: #5,2,3
                    if topLeft in outputDigitChars:
                        digitVal = 5
                    elif botLeft in outputDigitChars:
                        digitVal = 2
                    else:
                        digitVal = 3
                case 6: #0,6,9
                    if botLeft not in outputDigitChars:
                        digitVal = 9
                    elif topRight not in outputDigitChars:
                        digitVal = 6

            outputNumber += digitVal * outputTens
            outputTens /= 10
    
    outputSum += outputNumber
print(f'Sum of output values: {outputSum}')