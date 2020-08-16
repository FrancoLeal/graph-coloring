import random
import numpy as np

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
	rank = 0
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


def createNeighboor1(solutionOriginal):
	solution = np.copy(solutionOriginal)
	lenSolution = len(solution)
	x1,x2 = random.sample(list(range(0,lenSolution)),2)
	
	#print("Cambiando colores de nodos {0} y {1}".format(x1, x2))
	aux = solution[x1]
	solution[x1] = solution[x2]
	solution[x2] = aux
	return solution

def createNeighboor2(problem,solutionOriginal):
	value = 1
	solution = np.copy(solutionOriginal)
	lenSolution = len(solution)
	while value != 0:
		node1,node2 = random.sample(list(range(0,lenSolution)),2)
		value = problem[node1][node2]
	#print("Cambiando colores de nodos {0} y {1}".format(node1, node2))
	color1 = solution[node1]
	color2 = solution[node2]
	solution[node1] = color2
	solution[node2] = color1
	return solution

def createNeighboor3(solution):
	lenSolution = len(solution)
	position = random.randint(0,lenSolution-1)
	color = random.randint(0,lenSolution)
	newSolution = np.copy(solution)
	newSolution[position] = color
	return newSolution

def createPopulation(problem,solution,nNeighboors):
	population = []
	for i in range(0,nNeighboors):
		solution = createNeighboor3(solution)
		rank = rankSolution(problem,solution)
		solutionWithFitness = np.array([rank,solution])
		population.append(solutionWithFitness)
	return np.array(population)