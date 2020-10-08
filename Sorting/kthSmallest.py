# programa para encontrar o k-esimo menor elemento do vetor
# usando apenas particao

import random

def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux

def particao(V, p, n):

	if (p >= n): return 

	pivot = V[p] 		# pos. inicial vai ser o pivot
	i = p + 1 		 	
	j = n 				

	while (i <= j):
		if (V[i] > pivot and V[j] <= pivot):
			swap(V, i, j)
		if (V[i] <= pivot): i+=1
		if (V[j] > pivot): j-=1

	swap(V, p, j) # colocar o pivo na posicao correta

	particao(V, p, j-1)
	particao(V, j+1, n)

def achar(v, k):
	particao(v, 0, len(v)-1)
	print("Lista: {} \nK-esimo Elemento: {}".format(v, v[k-1]))

# main 

list = []

for x in range(20):
	list.append(random.randint(1, 10000))

list2 = [10, 133, 1313, 41, 23, 0, 2, 3 , 100]

achar(list2, 5)