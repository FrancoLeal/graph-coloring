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
from utils import mySort
import sudoku
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

originalRank, flag = rankSolution(graph, solution)
print("Ranking original: ",originalRank)

##########################
# Vecindad primera forma #
##########################

print("\nPrimer vecino, forma 1:")
solutionNeighboor1 = createNeighboor1(solution)
print(solutionNeighboor1)
plotFunctions.plotAdjacencyMatrix(graph,solution,'Vecino forma 1', labels)


firstFormRanking = [[],[]]
iteration = []
# Crear 100 vecinos
for i in range(0,100):
	solutionNeighboor1 = createNeighboor1(solutionNeighboor1)
	rank, flag = rankSolution(graph, solutionNeighboor1)
	firstFormRanking[0].append(rank)
	firstFormRanking[1].append(flag)
	iteration.append(i)
plotFunctions.plotRanks(firstFormRanking,iteration,'Vecindad primera forma, desordenado', False, originalRank)
# Ranking ordenado
rankSorted, iterationSorted = mySort(firstFormRanking, iteration)

plotFunctions.plotRanks(rankSorted,iterationSorted,'Vecindad primera forma, ordenado', True, originalRank)
##########################
# Vecindad segunda forma #
##########################

print("\nPrimer vecino, forma 2:")
solutionNeighboor2 = createNeighboor2(graph,solution)
print(solutionNeighboor2)

plotFunctions.plotAdjacencyMatrix(graph,solution,'Vecino forma 2', labels)

secondFormRanking = [[],[]]
iteration = []
# Crear 100 vecinos
for i in range(0,100):
	solutionNeighboor2 = createNeighboor2(graph,solutionNeighboor2)
	rank, flag = rankSolution(graph, solutionNeighboor2)
	secondFormRanking[0].append(rank)
	secondFormRanking[1].append(flag)
	iteration.append(i)
plotFunctions.plotRanks(secondFormRanking,iteration,'Vecindad segunda forma, desordenado', False, originalRank)

# Ranking ordenado
rankSorted, iterationSorted = mySort(secondFormRanking, iteration)

plotFunctions.plotRanks(rankSorted,iterationSorted,'Vecindad segunda forma, ordenado', True, originalRank)

##########################
# Vecindad tercera forma #
##########################

print("\Tercer vecino, forma 1:")
solutionNeighboor3 = createNeighboor3(solution)
print(solutionNeighboor3)

plotFunctions.plotAdjacencyMatrix(graph,solutionNeighboor3,'Vecino forma 3', labels)

thirdFormRanking = [[],[]]
iteration = []
# Crear 100 vecinos
for i in range(0,100):
	solutionNeighboor3 = createNeighboor3(solutionNeighboor3)
	rank, flag = rankSolution(graph, solutionNeighboor3)
	thirdFormRanking[0].append(rank)
	thirdFormRanking[1].append(flag)
	iteration.append(i)
plotFunctions.plotRanks(thirdFormRanking,iteration,'Vecindad tercera forma, desordenado', False, originalRank)

# Ranking ordenado
rankSorted, iterationSorted = mySort(thirdFormRanking, iteration)

plotFunctions.plotRanks(rankSorted,iterationSorted,'Vecindad tercera forma, ordenado', True, originalRank)

"""
#GA
# Funcion que devuelve los n mejores padres, m padres aleatorios y p padres con menos colores
def selectParents(population,nTopParents,nRandomParents,nLessColors):
	newPopulation = []
	sortedPopulation = population[population[:,0].argsort()[::-1]]
	#print(sortedPopulation)
	topPopulation = sortedPopulation[0:nTopParents]
	for i in range(0,nRandomParents):
		pos = random.randint(0,len(sortedPopulation)-1)
		newPopulation.append(sortedPopulation[pos])
	sortedPopulationByColors = population[population[:,1].argsort()]
	#print("++++++++++++++++++++++++++++++++++++")
	#print(sortedPopulation)
	#print("*****************************")
	lessColorPopulation = sortedPopulation[0:nLessColors]
	newPopulation = np.array(newPopulation)
	newPopulation = np.concatenate((newPopulation,topPopulation,lessColorPopulation))
	return newPopulation
def mutate(solution):
	for i in range(0,len(solution)):
		prob = random.random()
		if(prob<0.1):
			solution[i]=random.randint(0,len(solution)-1)
	return solution 
#Funcion que dados dos padres genera dos hijos, con 1% de prob de mutacion
def reproduce(problem,population,nChilds):
	i = 0
	newPopulation = []
	for i in range(0,nChilds):
		lenPop = len(population)
		parent1 = population[random.randint(0,lenPop-1)]
		parent2 = population[random.randint(0,lenPop-1)]
		position = random.randint(2,len(parent1[2])-2)
		infoParent1 = parent1[2][0:position]
		infoParent2 = parent2[2][position:len(parent2[2])]
		infoParent1 = np.array(infoParent1)
		infoParent2 = np.array(infoParent2)
		child1 = np.concatenate((infoParent1,infoParent2))
		infoParent2 = parent2[2][0:position]
		infoParent1 = parent1[2][position:len(parent2[2])]
		infoParent2 = np.array(infoParent2)
		infoParent1 = np.array(infoParent1)
		child2 = np.concatenate((infoParent2,infoParent1))
		mutate1 = random.random()
		if mutate1<0.01:
			child1 = mutate(child1)
		mutate2 = random.random()
		if mutate2<0.01:
			child2 = mutate(child2)
		newPopulation.append(np.array([rankSolution(problem,child1),len(np.unique(child1)),child1]))
		newPopulation.append(np.array([rankSolution(problem,child2),len(np.unique(child2)),child2]))
		
	return np.array(newPopulation)
#Funcion que elije 20 padres con menos colores, 20 padres aleatorios, 25 hijos con menos colores y 24 hijos aleatorios
def replace(oldPop,child):
	newPop = []
	sortedOldByColors = oldPop[oldPop[:,1].argsort()]
	topOldPop = sortedOldByColors[0:20]
	selectedOldPop = random.sample(list(oldPop),20)
	sortedChildByColors = child[child[:,1].argsort()]
	topChildPop = sortedChildByColors[0:25]
	selectedChild = random.sample(list(child),35)
	topOldPop = np.array(topOldPop)
	topChildPop = np.array(topChildPop)
	selectedOldPop = np.array(selectedOldPop)
	selectedChild = np.array(selectedChild)

	newPop = np.concatenate((topOldPop,topChildPop,selectedChild,selectedOldPop))
	return newPop

"""
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
"""
graph = sudoku.sudoku
print("**************************************")
print("****************Creando solucion inicial**************")
print("**************************************")
solution = createsolution(len(graph[0]))
print("**************************************")
print("****************Creando Poblacion**************")
print("**************************************")

nPop = 200
nRandom = 60
nTop = 40
nParentsToRep = 100

population = createPopulation(graph,solution,nPop)


nIterations = 1000
i = 0
print("**************************************")
print("****************Iterando**************")
print("**************************************")
while i < nIterations:
	print(i)
	#print("**************************************")
	#print("****************Parents**************")
	#print("**************************************")
	parents = selectParents(population,nTop,nRandom,0)
	#print("**************************************")
	#print("****************Reproduce**************")
	#print("**************************************")
	childPopulation = reproduce(graph,parents,nParentsToRep)
	#print("**************************************")
	#print("****************REplace**************")
	#print("**************************************")
	population = replace(parents,childPopulation)
	i=i+1
	print(population[population[:,1].argsort()])
	