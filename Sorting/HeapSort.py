
def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux

# - HeapSort -

def insercao_heap(V, elem, i): 	# inserir em ordem
	
	V[i] = elem
	k = i

	while (k >= 1):
		pai = k / 2
		if (V[pai] < V[k]):
			swap(V, pai, k)
		k = pai

def remocao_heap(V, i): 		# remover o maior elemento e organizar a heap
	
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

def heapify(lista): 				# criar a heap max
	
	for i in range(0, len(lista)):
		insercao_heap(lista, lista[i], i)


def HeapSort(lista): 				# remover os elementos da heap max 
	heapify(lista)

	for i in range (len(lista)-1, 0, -1):
		lista[i] = remocao_heap(lista, i)

	print("HeapSort: {}".format(lista))