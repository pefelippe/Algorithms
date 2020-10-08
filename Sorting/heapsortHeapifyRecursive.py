import random

def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux	

# VERSAO RECURSIVA

def Heapify_Recursivo(V, i , n):

	if (i == n): return
	k = i
	while (k >= 1):
		pai = k / 2
		if (V[pai] < V[k]):
			swap(V, pai, k)
		k = pai

	Heapify_Recursivo(V, i+1, n)

def Heapsort(lista):
	Heapify_Recursivo(lista, 0, len(lista) - 1)

	for i in range (len(lista)-1, 0, -1):
		lista[i] = Remocao_Heap(lista, i)

	print("HeapSort: {}".format(lista))

def Remocao_Heap(V, i): 		# remover o maior elemento e organizar a heap
	
	aux = V[0]
	swap(V, 0, i)  	# maior elemento vai pro final da lista
					# agora precisamos tornar novamente a heap em max-heap
	i-=1			
	k = 0

	while (2 * k <= i and i != 0):
		filho1 = 2 * k 
		filho2 = 2 * k + 1

		if (i == 2 * k or V[filho1] > V[filho2]):
			if (V[k] < V[filho1]):
				swap(V, k, filho1)
			k = filho1
		else:
			if (V[k] < V[filho2]):
				swap(V, k, filho2)
			k = filho2

	return aux

### MAIN

list = []

for x in range(20):
	list.append(random.randint(1, 10000))

list2 = [10, 133, 1313, 41, 23, 0, 2, 3 , 100]

Heapsort(list2)
