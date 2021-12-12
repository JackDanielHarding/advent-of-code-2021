from re import match
from collections import Counter

with open("./input.txt", "r") as inputFile:
    pathsStr = inputFile.read().splitlines()
    
graph = dict()
for pathStr in pathsStr:
    m = match('([a-zA-Z]+)-([a-zA-Z]+)', pathStr)
    nodeSrc = m.group(1)
    nodeDst = m.group(2)
    
    if nodeSrc not in graph:
        graph[nodeSrc] = list()
        
    if nodeDst not in graph:
        graph[nodeDst] = list()
    
    if nodeDst != "start":
        graph[nodeSrc].append(nodeDst)
    if nodeSrc != "start":
        graph[nodeDst].append(nodeSrc)
    
    
def smallCavesOnlyOnceCheck(nextNode : str, visited : list[str]):
    return nextNode.isupper() or nextNode not in visited

def oneSmallCaveTwiceOnlyCheck(nextNode : str, visited : list[str]):
    if nextNode.isupper():
        return True
    else:
        smallCavesVisited = [node for node in visited if node.islower()]
        if nextNode not in smallCavesVisited:
            return True
        else:
            countedSmallCaves = Counter(smallCavesVisited).most_common()
            return len(countedSmallCaves) == 0 or countedSmallCaves[0][1] <= 1

def countPaths(graph : dict[str, list[str]], node : str, visited : list[str], validNextNodeTest):
    if node == "end":
        return 1
 
    pathsFromNodeToEnd = 0
    visited.append(node)
    
    nodesToVisit = [nextNode for nextNode in graph.get(node, list()) if validNextNodeTest(nextNode, visited)]
    for nextNode in nodesToVisit:
        pathsFromNodeToEnd += countPaths(graph, nextNode, visited, validNextNodeTest)
 
    for i, visitedNode in reversed(list(enumerate(visited))):
        if visitedNode == node:
            del visited[i]
            break
 
    return pathsFromNodeToEnd

visited = list()
print(f'Number of unique paths if small caves can only be visited once: {countPaths(graph, "start", visited, smallCavesOnlyOnceCheck)}')
print(f'Number of unique paths if one small cave can be visited twice: {countPaths(graph, "start", visited, oneSmallCaveTwiceOnlyCheck)}')

