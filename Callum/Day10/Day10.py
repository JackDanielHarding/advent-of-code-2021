with open("./input.txt", "r") as inputFile:
    inputStrs = inputFile.read().splitlines()

incompleteStacks = []
error=0
for idx, line in enumerate(inputStrs):
    lineStack = []
    for char in line:
        match char:
            case '(' | '[' | '{' | '<':
                lineStack.append(char)
            case ')':
                open = lineStack.pop()
                if open != '(':
                    error += 3
                    break
            case ']':
                open = lineStack.pop()
                if open != '[':
                    error += 57
                    break
            case '}':
                open = lineStack.pop()
                if open != '{':
                    error += 1197
                    break
            case '>':
                open = lineStack.pop()
                if open != '<':
                    error += 25137
                    break
    else:
        incompleteStacks.append(lineStack)
        continue
        
print(f'Corrupted Error Score: {error}')

incompleteLineScores = []
for lineStack in incompleteStacks:
    lineScore = 0
    for char in reversed(lineStack):
        lineScore *= 5
        match char:
            case '(':
                lineScore += 1
            case '[':
                lineScore += 2
            case '{':
                lineScore += 3
            case '<':
                lineScore += 4
                
    incompleteLineScores.append(lineScore)
    
incompleteLineScores.sort()
print(f'Middle incomplete line Score: {incompleteLineScores[len(incompleteLineScores)//2]}')