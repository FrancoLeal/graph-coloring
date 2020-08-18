# Funcion para ordenar al mismo tiempo la iteracion y el ranking
def mySort(rankingList, iterationList):
	sortedRankingList = [[],[]]
	sortedIterationList = []
	while len(rankingList[0]) != 0:
		minimun = rankingList[0][0]
		i = 0
		pos = 0
		while i<len(rankingList[0]):
			if(minimun > rankingList[0][i]):
				minimun = rankingList[0][i]
				pos = i
			i += 1
		sortedRankingList[0].append(rankingList[0][pos])
		sortedRankingList[1].append(rankingList[1][pos])
		sortedIterationList.append(iterationList[pos])
		rankingList[0].pop(pos)
		rankingList[1].pop(pos)
		iterationList.pop(pos)
	return sortedRankingList, sortedIterationList