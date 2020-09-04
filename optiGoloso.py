import sudoku
import numpy as np
from neighborFunctions import rankSolution
import timeit
import random
import plotFunctions
#Your statements here

file = open("myciel3.col","r")
nNodes= 0
graph = []
for line in file:
	if line[0]=="p":
		line = line.split()
		nNodes = int(line[2])
		graph = np.zeros((nNodes,nNodes),dtype=np.int16)
	if line[0]=="e":
		line = line.split()
		graph[int(line[1])-1][int(line[2])-1] = 1
		graph[int(line[2])-1][int(line[1])-1] = 1

graph = sudoku.sudoku
g = dict()
i = 0
while i < len(graph):
    j = 0
    listAux = []
    while j < len(graph):
        if(graph[i][j] == 1):
            listAux.append(j)
        g[i] = listAux
        j = j + 1
    i = i + 1
def first_available(color_list):
    """Return smallest non-negative integer not in the given list of colors."""
    color_set = set(color_list)
    count = 0
    while True:
        if count not in color_set:
            return count
        count += 1
        
def greedy_color(G, order):
    """Find the greedy coloring of G in the given order.
    The representation of G is assumed to be like https://www.python.org/doc/essays/graphs/
    in allowing neighbors of a node/vertex to be iterated over by "for w in G[node]".
    The return value is a dictionary mapping vertices to their colors."""
    color = dict()
    for node in order:
        used_neighbour_colors = [color[nbr] for nbr in G[node]
                                 if nbr in color]
        color[node] = first_available(used_neighbour_colors)
    return color

nodes = list(range(0, len(g)))
start = timeit.default_timer()
ranksList = []
colorsList = []
iteration = []
for i in range(0, 1000):
    randomOrder = random.sample(nodes, len(nodes))
    color = greedy_color(g, randomOrder)
    solution = list(range(0, len(g)))
    for key, value in color.items():
        solution[key] = value
    rank = rankSolution(graph, solution)
    nColors = len(np.unique(solution))
    ranksList.append(rank)
    colorsList.append(nColors)
    iteration.append(i)

plotFunctions.plotGreedy(iteration, ranksList, colorsList, 'sudoku')
stop = timeit.default_timer()
print('Time: ', stop - start)
