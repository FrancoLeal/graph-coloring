import random
import numpy as np
from scipy import stats
def createsolution(nNodes):
	count = 0
	solution = []
	while count < nNodes:
		solution.append(random.randint(0,nNodes))
		count += 1
	solution = np.array(solution)
	return solution

def createsolution(nNodes):
	count = 0
	solution = []
	while count < nNodes:
		solution.append(random.randint(0,nNodes-1))
		count += 1
	solution = np.array(solution)
	return solution


def rankSolution(problem,solution):
	flag = True
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
					flag = False
			node2 += 1
		node1 += 1
	return rank, flag


def createNeighboor1(solutionOriginal):
	solution = np.copy(solutionOriginal)
	option = random.randint(1,2)
	# Si es 1, solo se cambia el color de los nodos
	if(option == 1):
		print("Realizando swap de colores...")
		lenSolution = len(solution)
		x1,x2 = random.sample(list(range(0,lenSolution)),2)
		aux = solution[x1]
		solution[x1] = solution[x2]
		solution[x2] = aux

	# Si es 2, solo se agrega o se elimina un color a la solucion
	if(option == 2):
		option = random.randint(1,2)
		colors = np.unique(solution)
		# Se agrega
		if(option == 1):
			# verificar que es posible añadir
			if(len(colors) == len(solution)):
				# Realizar cambio de color solamente
				print("Realizando swap de colores...")
				lenSolution = len(solution)
				x1,x2 = random.sample(list(range(0,lenSolution)),2)
				aux = solution[x1]
				solution[x1] = solution[x2]
				solution[x2] = aux
				return solution
			print("Agregando color...")
			nNodes = len(solution)
			randomColor = random.randint(0, nNodes-1)
			while randomColor in solution:
				randomColor = random.randint(0, nNodes-1)
			m = stats.mode(solution)[0][0]
			positionList = np.where(solution == m)[0]
			pos = positionList[random.randint(0,len(positionList)-1)]
			solution[pos] = randomColor
		# Se elimina
		else:
			if(len(colors) == 1):
				# Realizar cambio de color solamente
				print("Realizando swap de colores...")
				lenSolution = len(solution)
				x1,x2 = random.sample(list(range(0,lenSolution)),2)
				aux = solution[x1]
				solution[x1] = solution[x2]
				solution[x2] = aux
				return solution
			print("Eliminando color...")
			colorsAux = random.sample(list(colors),2)
			i = 0
			while i < len(solution):
				if solution[i] == colorsAux[0]:
					solution[i] = colorsAux[1]
				i = i+1
	return solution

def createNeighboor2(problem,solutionOriginal):
	value = 1
	solution = np.copy(solutionOriginal)
	lenSolution = len(solution)
	option = random.randint(1,2)

	if option == 1:
		print("Realizando swap de colores...")
		while value != 0:
			node1,node2 = random.sample(list(range(0,lenSolution)),2)
			value = problem[node1][node2]
			if(value == 1):
				if(solution[node1] == solution[node2]):
					value = 0
				else:
					value = 1
		color1 = solution[node1]
		color2 = solution[node2]
		solution[node1] = color2
		solution[node2] = color1

	# Si es 2, solo se agrega o se elimina un color a la solucion
	if(option == 2):
		option = random.randint(1,2)
		colors = np.unique(solution)
		# Se agrega
		if(option == 1):
			# verificar que es posible añadir
			if(len(colors) == len(solution)):
				# Realizar cambio de color solamente
				print("Realizando swap de colores...")
				while value != 0:
					node1,node2 = random.sample(list(range(0,lenSolution)),2)
					value = problem[node1][node2]
					if(value == 1):
						if(solution[node1] == solution[node2]):
							value = 0
						else:
							value = 1
				color1 = solution[node1]
				color2 = solution[node2]
				solution[node1] = color2
				solution[node2] = color1
				return solution
			print("Agregando color...")
			nNodes = len(solution)
			randomColor = random.randint(0, nNodes-1)
			while randomColor in solution:
				randomColor = random.randint(0, nNodes-1)
			m = stats.mode(solution)[0][0]
			positionList = np.where(solution == m)[0]
			pos = positionList[random.randint(0,len(positionList)-1)]
			solution[pos] = randomColor
		# Se elimina
		else:
			if(len(colors) == 1):
				# Realizar cambio de color solamente
				print("Realizando swap de colores...")
				while value != 0:
					node1,node2 = random.sample(list(range(0,lenSolution)),2)
					value = problem[node1][node2]
					if(value == 1):
						if(solution[node1] == solution[node2]):
							value = 0
						else:
							value = 1
				color1 = solution[node1]
				color2 = solution[node2]
				solution[node1] = color2
				solution[node2] = color1
				return solution
			print("Eliminando color...")
			colorsAux = random.sample(list(colors),2)
			i = 0
			while i < len(solution):
				if solution[i] == colorsAux[0]:
					solution[i] = colorsAux[1]
				i = i+1
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