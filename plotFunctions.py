import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.patches as mpatches
# Variable global para el contador de graficos
plot_index = 0


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

def plotRanks(ranking, xAxis, fileName, is_sorted, originalRank):
	global plot_index
	fig = plt.figure(figsize=(20, 6))
	if is_sorted:
		originalRankList = [str(originalRank)]*len(xAxis)
	else:
		originalRankList = [originalRank]*len(xAxis)

	i = 0
	while i<len(ranking[0]):
		x = [xAxis[i]]
		y = [ranking[0][i]]
		if is_sorted:
			x = [str(x[0])]
			y = [str(y[0])]
		if ranking[1][i]:
			color = 'green'
		else:
			color = 'red'
		plt.plot(x,y,linestyle='None',marker='.', color=color, markersize=10)
		i += 1
	plt.plot(xAxis,originalRankList,'b')
	fig.suptitle(fileName)
	plt.xticks(rotation = 50)
	plt.xlabel('Iteración')
	plt.ylabel('Ranking')

	# Legend

	red_patch = mpatches.Patch(color='red', label='Soluciones infactibles')
	green_patch = mpatches.Patch(color='green', label='Soluciones factibles')
	blue_patch = mpatches.Patch(color='blue', label='Ranking solución original')
	plt.legend(handles=[green_patch, red_patch, blue_patch])
	plt.savefig('plots/'+fileName+'.png', dpi=199)
	plot_index += 1
	plt.clf()