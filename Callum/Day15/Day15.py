
from numpy.lib.npyio import genfromtxt
from networkx.generators.lattice import grid_2d_graph
from networkx.algorithms.shortest_paths.astar import astar_path_length

weighted2DGrid = genfromtxt('./input_small.txt', delimiter=1, dtype=int)

width = weighted2DGrid.shape[1]
height = weighted2DGrid.shape[0]

def ManhattanHeuristic(startNode : tuple[int, int], endNode : tuple[int, int]) -> float :
    return abs(endNode[0] - startNode[0]) + abs(endNode[1] - startNode[1])

def TiledEdgeWeight(startNode: tuple[int, int], endNode: tuple[int, int], _) -> int :
    val = weighted2DGrid[endNode[0] % height, endNode[1] % width]
    tileHIndex = endNode[0] // height
    tileWIndex = endNode[1] // width
    val += tileHIndex + tileWIndex
    val = ((val-1) % 9) + 1
    return val

def FindLowestRisk(tiles, EdgeWeight):
    graph = grid_2d_graph(height * tiles, width * tiles)

    topLeft = (0,0)
    bottomRight = ((height * tiles) - 1, (width * tiles) - 1)

    shortestPathLength = astar_path_length(graph, topLeft, bottomRight, ManhattanHeuristic, EdgeWeight)

    print(f'Lowest total risk: {shortestPathLength}')

FindLowestRisk(1, TiledEdgeWeight)
FindLowestRisk(5, TiledEdgeWeight)