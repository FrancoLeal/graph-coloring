import random
import math
import plotFunctions
import numpy as np
from neighborFunctions import (
	createNeighboor1,
	createNeighboor2
)
	

#graph = np.zeros((16,16),dtype=int);
#print(graph)
def createsolution(nNodes):
	count = 0
	solution = []
	while count < nNodes:
		solution.append(random.randint(0,nNodes))
		count += 1
	solution = np.array(solution)
	return solution


def rankSolution(problem,solution):
	node1 = 0
	length = len(problem)
	rank = length - len(np.unique(solution)) + 1
	while node1 < length:
		# Para recorrer solo parte superior
		node2 = node1+1
		while node2 < length:
			value = problem[node1][node2]
			# Si hay conexion
			if(value == 1):
				# Se obtienen los colores de cada nodo
				colorNode1 = solution[node1]
				colorNode2 = solution[node2]
				if colorNode1 == colorNode2:
					rank -= 1
				
			node2 += 1
		node1 += 1
	return rank

graph = [
            #1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
			[0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0],
			[1 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0],
			[1 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0],
			[1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1],
			[1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0],
			[1 , 1 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0],
			[0 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0],
			[0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1],
			[1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0],
			[0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 0 , 0],
			[0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 0 , 1 , 1],
			[0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1],
			[1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 1],
			[0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 1 , 1],
			[0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 1],
			[0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0]
		]
"""
graph = [
	[0,1,0,0],
	[1,0,1,1],
	[0,1,0,1],
	[0,1,1,0],
]
"""

print("Matriz de adjacencia:")
for line in graph:
	print(line)

# Labels
labels = {}
for i in range(0, len(graph)):
	labels[i] = i
#####################
# Solucion Original #
#####################
print("\nSolucion:")
solution = createsolution(len(graph[0]))
print(solution)
plotFunctions.plotAdjacencyMatrix(graph,solution,'Grafo Original', labels)

rank = rankSolution(graph, solution)
print("Ranking original: ",rank)

##########################
# Vecindad primera forma #
##########################

print("\nPrimer vecino, forma 1:")
solutionNeighboor1 = createNeighboor1(solution)
print(solutionNeighboor1)
plotFunctions.plotAdjacencyMatrix(graph,solution,'Vecino forma 1', labels)


firstFormRanking = []
iteration = []
# Crear 100 vecinos
for i in range(0,100):
	solutionNeighboor1 = createNeighboor1(solutionNeighboor1)
	rank = rankSolution(graph, solutionNeighboor1)
	firstFormRanking.append(rank)
	iteration.append(i)
plotFunctions.plotRanks(firstFormRanking,iteration,'Vecindad primera forma, desordenado', False)

# Ranking ordenado
rankSorted, iterationSorted = zip(*sorted(zip(firstFormRanking, iteration)))

plotFunctions.plotRanks(rankSorted,iterationSorted,'Vecindad primera forma, ordenado', True)

##########################
# Vecindad segunda forma #
##########################

print("\nPrimer vecino, forma 2:")
solutionNeighboor2 = createNeighboor2(graph,solution)
print(solutionNeighboor2)

plotFunctions.plotAdjacencyMatrix(graph,solution,'Vecino forma 2', labels)

secondFormRanking = []
iteration = []
# Crear 100 vecinos
for i in range(0,100):
	solutionNeighboor2 = createNeighboor2(graph,solutionNeighboor2)
	rank = rankSolution(graph, solutionNeighboor2)
	secondFormRanking.append(rank)
	iteration.append(i)
plotFunctions.plotRanks(secondFormRanking,iteration,'Vecindad segunda forma, desordenado', False)

# Ranking ordenado
rankSorted, iterationSorted = zip(*sorted(zip(secondFormRanking, iteration)))

plotFunctions.plotRanks(rankSorted,iterationSorted,'Vecindad segunda forma, ordenado', True)

