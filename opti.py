import random
import math
import plotFunctions
import numpy as np
from neighborFunctions import (
	createNeighboor1,
	createNeighboor2,
	createNeighboor3,
	createPopulation,
	createsolution,
	rankSolution
)


#graph = np.zeros((16,16),dtype=int);
#print(graph)


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

plotFunctions.plotRanks(rankSorted,iterationSorted,'Vecindad segunda forma, ordenado', True)"""

#GA

def selectParents(population,nTopParents,nRandomParents):
	newPopulation = []
	sortedPopulation = population[population[:,0].argsort()[::-1]]
	topPopulation = sortedPopulation[0:nTopParents]
	for i in range(0,nRandomParents):
		pos = random.randint(0,len(sortedPopulation)-1)
		newPopulation.append(sortedPopulation[pos])
	newPopulation = np.array(newPopulation)
	newPopulation = np.concatenate((newPopulation,topPopulation))
	return newPopulation

def reproduce(problem,population,nChilds):
	i = 0
	newPopulation = []
	for i in range(0,nChilds):
		lenPop = len(population)
		parent1 = population[random.randint(0,lenPop-1)]
		parent2 = population[random.randint(0,lenPop-1)]
		position = random.randint(2,len(parent1[1])-2)
		infoParent1 = parent1[1][0:position]
		infoParent2 = parent2[1][position:len(parent2[1])]
		infoParent1 = np.array(infoParent1)
		infoParent2 = np.array(infoParent2)
		child1 = np.concatenate((infoParent1,infoParent2))
		infoParent2 = parent2[1][0:position]
		infoParent1 = parent1[1][position:len(parent2[1])]
		infoParent2 = np.array(infoParent2)
		infoParent1 = np.array(infoParent1)
		child2 = np.concatenate((infoParent2,infoParent1))
		mutate1 = random.random()
		if mutate1<0.01:
			child1 = createNeighboor3(child1)
		mutate2 = random.random()
		if mutate2<0.01:
			child2 = createNeighboor3(child2)
		newPopulation.append(np.array([rankSolution(problem,child1),child1]))
		newPopulation.append(np.array([rankSolution(problem,child2),child2]))
		
	return np.array(newPopulation)

def replace(oldPop,child):
	newPop = []
	selectedOldPop = random.sample(list(oldPop),40)
	selectedChild = random.sample(list(child),60)
	selectedOldPop = np.array(selectedOldPop)
	selectedChild = np.array(selectedChild)

	newPop = np.concatenate((selectedChild,selectedOldPop))
	return newPop


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

solution = createsolution(len(graph[0]))
population = createPopulation(graph,solution,100)


nIterations = 100
i = 0
while i < nIterations:
	parents = selectParents(population,10,40)
	childPopulation = reproduce(graph,parents,50)
	population = replace(parents,childPopulation)
	i=i+1
print(population)