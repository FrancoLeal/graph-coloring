#import numpy as np
import random
import math

#graph = np.zeros((16,16),dtype=int);
#print(graph)
def createsolution(nNodes):
	count = 0
	nColors = math.sqrt(nNodes)
	solution = []
	while count < nNodes:
		solution.append(random.randint(0,nColors))
		count += 1
	return solution

def createNeighboor1(solution):
	lenSolution = len(solution)
	x1 = random.randint(0,lenSolution-1)
	x2 = random.randint(0,lenSolution-1)
	aux = solution[x1]
	solution[x1] = solution[x2]
	solution[x2] = aux
	return solution

def createNeighboor2(problem,solution):
	value = 0
	node1 = 0
	node2 = 0
	lenSolution = len(solution)
	while value != 1:
		node1 = random.randint(0,lenSolution-1)
		node2 = random.randint(0,lenSolution-1)
		value = problem[node1][node2]
	print("node1 ", node1 , " node2 ", node2)
	color1 = solution[node1]
	color2 = solution[node2]
	solution[node1] = color2
	solution[node2] = color1
	return solution



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

for line in graph:
	print(line)
solution = createsolution(len(graph[0]))
print(solution)

solutionNeighboor1 = createNeighboor1(solution)
print(solutionNeighboor1)

solutionNeighboor2 = createNeighboor2(graph,solution)
print(solutionNeighboor2)
