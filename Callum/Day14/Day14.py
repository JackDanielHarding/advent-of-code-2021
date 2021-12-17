with open("./input.txt", "r") as inputFile:
    input = inputFile.read()
    
inputSplit = input.split("\n\n")
polymer = inputSplit[0]

rules = inputSplit[1].splitlines()
matchRules = {rule[0:2]:(rule[0]+rule[6:7], rule[6:7]+rule[1], rule[0], rule[1]) for rule in rules}

def GetElementCountsAfterNIters(polymer, matchRules, n):
    elementCounts = {rule[6:7]:0 for rule in rules}
    pairCounts = {pair:0 for pair in matchRules}

    for charIndex in range(len(polymer)-1):
        pair = polymer[charIndex:charIndex+2]
        pairCounts[pair] += 1
    
    for i in range(n):
        newPairCounts = {pair:0 for pair in matchRules}
        for pair, newPairs in matchRules.items():
            pairCount = pairCounts[pair]
            newPairCounts[newPairs[0]] += pairCount
            newPairCounts[newPairs[1]] += pairCount
        pairCounts = newPairCounts
    
    for pair, (_, _, firstLetter, secondLetter) in matchRules.items():
        pairCount = pairCounts[pair]
        elementCounts[firstLetter] += pairCount
        elementCounts[secondLetter] += pairCount

    elementCounts[polymer[0]] += 1
    elementCounts[polymer[-1]] += 1

    return {letter:count//2 for letter,count in elementCounts.items()}

part1Iters = 10
part1ElementCounts = GetElementCountsAfterNIters(polymer, matchRules, part1Iters)

print(f'Difference in max and min occurence element after {part1Iters} iterations: {max(part1ElementCounts.values()) - min(part1ElementCounts.values())}')

part2Iters = 40
part2ElementCounts = GetElementCountsAfterNIters(polymer, matchRules, part2Iters)

print(f'Difference in max and min occurence element after {part2Iters} iterations: {max(part2ElementCounts.values()) - min(part2ElementCounts.values())}')