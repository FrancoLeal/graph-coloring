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
import scipy
#graph = np.zeros((16,16),dtype=int);
#print(graph)
"""
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

graph = [
	[0,1,0,1],
	[1,0,1,1],
	[0,1,0,1],
	[1,1,1,0],
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
	randomList = random.sample(range(nTopParents, len(population)), nRandomParents)
	for i in randomList:
		newPopulation.append(sortedPopulation[i])
	sortedPopulationByColors = population[population[:,1].argsort()]
	#print("++++++++++++++++++++++++++++++++++++")
	#print(sortedPopulation)
	#print("*****************************")
	lessColorPopulation = sortedPopulation[0:nLessColors]
	newPopulation = np.array(newPopulation)
	newPopulation = np.concatenate((newPopulation,topPopulation,lessColorPopulation))
	return newPopulation
def mutate(solution):
	solution = createNeighboor3(solution)
	return solution

def mix(parent1,parent2):
	positionList = random.sample(range(0, len(parent1[2])),2)
	position1 = min(positionList)
	position2 = max(positionList)
	child1 = []
	child2 = []
	for i in range(0,len(parent1[2])):
		if(i<position1 or i>position1):
			child1.append(parent1[2][i])
			child2.append(parent2[2][i])
		else:
			child1.append(parent2[2][i])
			child2.append(parent1[2][i])
	child1 = np.array(child1)
	child2 = np.array(child2)
	return child1,child2
		
#Funcion que dados dos padres genera dos hijos, con 1% de prob de mutacion
def reproduce(problem,population,nChilds):
	i = 0
	newPopulation = []
	for i in range(0,nChilds):
		lenPop = len(population)
		positionsList = random.sample(range(0, lenPop), 2)
		parent1 = population[positionsList[0]]
		parent2 = population[positionsList[1]]
		child1,child2 = mix(parent1,parent2)
		mutate1 = random.random()
		if mutate1<0.01:
			child1 = mutate(child1)
		mutate2 = random.random()
		if mutate2<0.01:
			child2 = mutate(child2)
		newPopulation.append(np.array([rankSolution(problem,child1),len(np.unique(child1)),child1]))
		newPopulation.append(np.array([rankSolution(problem,child2),len(np.unique(child2)),child2]))
		"""
		print("Colores hijo 1: ",len(np.unique(child1)))
		print("Colores hijo 2: ",len(np.unique(child2)))
		print("Ranking hijo 1: ",rankSolution(problem,child1))
		print("Ranking hijo 2: ",rankSolution(problem,child2))
		"""
	return np.array(newPopulation)
#Funcion que elije 20 padres con menos colores, 20 padres aleatorios, 25 hijos con menos colores y 24 hijos aleatorios
def replace(oldPop,child,nTopOld,nTopChild,nRandomOld,nRandomChild):
	newPop = []
	sortedOldByColors = oldPop[oldPop[:,1].argsort()]
	topOldPop = sortedOldByColors[0:nTopOld]
	selectedOldPop = random.sample(list(oldPop),nRandomOld)
	sortedChildByColors = child[child[:,1].argsort()]
	topChildPop = sortedChildByColors[0:nTopChild]
	selectedChild = random.sample(list(child),nRandomChild)
	topOldPop = np.array(topOldPop)
	topChildPop = np.array(topChildPop)
	selectedOldPop = np.array(selectedOldPop)
	selectedChild = np.array(selectedChild)

	newPop = np.concatenate((topOldPop,topChildPop,selectedChild,selectedOldPop))
	return newPop

def findBest(actualBest,population):
	if len(actualBest)==0:
		actualBest = population[0]
	aux = True
	for element in population:
		if element[0][1]:
			if not actualBest[0][1]:
				actualBest=element
			elif actualBest[0][0]<element[0][0]:
				actualBest=element
			aux = False
	for element in population:
		if aux:
			if actualBest[0][0]<element[0][0]:
				actualBest=element
	return actualBest
"""
file = open("queen5_5.col","r")
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
# Labels
labels = {}
for i in range(0, len(graph)):
	labels[i] = i
print("**************************************")
print("****************Creando solucion inicial**************")
print("**************************************")
solution = createsolution(len(graph[0]))
print("**************************************")
print("****************Creando Poblacion**************")
print("**************************************")

nPop = 300
nRandom = 120
nTop = 30
nParentsToRep = 150
allData = []
allDataColors = []
generationsAux = []
means = []
meansColors = []
for v in range(1,12):
	population = createPopulation(graph,solution,nPop)

	nIterations = 100
	i = 0
	print("**************************************")
	print("***Prueba N°: ",v,"***")
	print("**************************************")
	best = []
	bestOriginalRank = findBest(best,population)
	plotFunctions.plotAdjacencyMatrix(graph,bestOriginalRank[-1],'Primera versión', labels)
	generations = []
	ranks = []
	nColors = []
	meanDataAux = []
	while i < nIterations:
		#print(i)
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
		population = replace(parents,childPopulation,30,30,120,120)
		best = findBest(best,population)
		generations.append(i+1)
		ranks.append(best[0])
		nColors.append(best[1])
		i=i+1
		# Se agregan todos los rankins y los colores, ya que en los otros arreglos
		# se pierden
		allData.append(best[0])
		allDataColors.append(nColors[0])
		generationsAux.append(i)
	plotFunctions.plotGenerationRanking(ranks, generations, "Generaciones vs Ranking "+str(v), bestOriginalRank[0][0], False)
	plotFunctions.plotNColors(generations, nColors, "Generaciones vs Cantidad Colores  "+str(v))
	plotFunctions.plotAdjacencyMatrix(graph,best[-1],'Ultima versión', labels)
# Como primero se calcula cada iteración de cada generación, es necesario hacer
# este proceso para calcular los promedios, lo que hace es que toma los datos
# correspondiente a su generación solamente
for i in range(0, nIterations):
	j = 0
	meanDataAux=[]
	meanColorsAux=[]
	while j<len(allData):
		if(j%nIterations==0):
			meanDataAux.append(allData[j+i][0])
			meanColorsAux.append(allDataColors[j+1])
		j = j+1
	means.append(scipy.mean(meanDataAux))
	meansColors.append(scipy.mean(meanColorsAux))
print(allDataColors)
print(meanColorsAux)
plotFunctions.plotFinals(generations,generationsAux,allData,means,'TEST')
plotFunctions.plotFinalsColors(generations,generationsAux,allDataColors,meansColors,'TEST2')