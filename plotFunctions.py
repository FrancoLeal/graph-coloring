import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Variable global para el contador de graficos
plot_index = 1

# Convertir de numeros a string
def try_str(x):
    try:
        return str(x)
    except ValueError:
        return x
# Se dibuja el grafo
def plotAdjacencyMatrix(adjacency_matrix, solution, fileName, labels):
	adjacency_matrix = np.array(adjacency_matrix)
	rows, cols = np.where(adjacency_matrix == 1)
	edges = zip(rows.tolist(), cols.tolist())
	gr = nx.Graph()
	gr.add_edges_from(edges)
	nx.draw(gr, node_size=500, labels=labels, node_color=solution)
	# Matplotlib
	plt.savefig('plots/'+fileName+'.png')
	plt.clf()

def plotRanks(ranking, xAxis, fileName, is_sorted):
	global plot_index
	fig = plt.figure(plot_index, figsize=(20, 6))
	if is_sorted:
		xAxis = [try_str(x) for x in xAxis]
		ranking = [try_str(x) for x in ranking]
	plt.plot(xAxis,ranking,linestyle='None',marker='.')
	fig.suptitle(fileName)
	plt.xticks(rotation = 50)
	plt.xlabel('Iteración')
	plt.ylabel('Ranking')
	plt.savefig('plots/'+fileName+'.png', dpi=199)
	plot_index += 1
	plt.clf()