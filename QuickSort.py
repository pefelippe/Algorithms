
def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux

def QuickSort(lista):
	quick(lista, 0, len(lista) - 1)

	print('Lista Ordenada [QuickSort] =  {} '.format(lista))

def particao(V, i, j):

	pos = i 		# primeira posicao eh o pivot
	pivot = V[pos] 

	i+= 1 		 # incrementa p passar pra prox pos. 

	while (i <= j):
		if (V[i] > pivot and V[j] <= pivot):
			swap(V, i, j)
		if (V[i] <= pivot): i+=1
		if (V[j] > pivot): j-=1
	
	swap(V, pos, j)
	return j

def quick(lista, posIni, posFinal):
	if (posIni >= posFinal): return
	k = particao(lista, posIni, posFinal)
	quick(lista, posIni, k-1)
	quick(lista, k+1, posFinal)
