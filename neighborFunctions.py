import random

def createNeighboor1(solution):
	lenSolution = len(solution)
	x1,x2 = random.sample(list(range(0,lenSolution)),2)
	
	#print("Cambiando colores de nodos {0} y {1}".format(x1, x2))
	aux = solution[x1]
	solution[x1] = solution[x2]
	solution[x2] = aux
	return solution

def createNeighboor2(problem,solution):
	value = 1
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