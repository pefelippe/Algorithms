import random

def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux

def DualPivotQuicksort(lista):
	print("Lista Desordenada: {}".format(lista))
	DualPivotQuick(lista, 0, len(lista) - 1)
	print("Lista Ordenada: {}".format(lista))

def DualPivotQuick(lista, posIni, posFinal):
	if (posIni < posFinal):
		K1, K2 = DualPivotPartition(lista, posIni, posFinal)
		DualPivotQuick(lista, posIni, K1-1)
		DualPivotQuick(lista, K1+1, K2-1)
		DualPivotQuick(lista, K2+1, posFinal)

def DualPivotPartition(lista, posIni, posFinal):
	# na verdade, nao esta fucionando mt bem.
	# ideia: 1) colocar todos os elementos < que p_esq no comeco da lista
	#		 2) colocar todos os elementos >= que p_dir no final da lista
	#		 3) trocar de posicao p_esq pelo ultimo elemento menor que ele 
	#		 4) trocar de posicao p_dir pelo ultimo elemento maior que ele

	#if (lista[posIni] > lista[posFinal]): 
	#	swap(lista, posIni, posFinal)

	p_esq = posIni			# pos. pivo esquerda
	p_dir = posFinal		# pos. pivo direita
	atual = posIni + 1		# pos. do elemento atual	
	elemE = posIni + 1		# pos. prox elemento esquerda
	elemD = posFinal - 1	# pos. prox elemento direita

	while (atual <= elemD):

		if(lista[atual] < lista[p_esq]): 		# se o elemento for menor que pivo da esquerda
			swap(lista, elemE, atual)
			elemE += 1
			
		elif (lista[atual] >= lista[p_dir]):	# se elem maior ou igual que o pivo da direita

			while (lista[elemD] > lista[p_dir] and atual < elemD): # procurar a posicao correta
				elemD -= 1
			swap(lista, atual, elemD)
			elemD -= 1

			if (lista[atual] < lista[p_esq]):
				swap(lista, atual, elemE)
				elemE +=1

		atual += 1
	
	elemE -= 1
	elemD += 1
	swap(lista, p_esq, elemE) # troca pela ultima posicao com elementos menores que p_esq
	swap(lista, p_dir, elemD) # troca pela ultima posicao com elementos maiores que p_dir

	return elemE, elemD

# main

list = []

for x in range(10):
	list.append(random.randint(1, 10000))

list2 = [10, 133, 1313, 41, 23, 0, 2, 3 , 100]


DualPivotQuicksort(list)
DualPivotQuicksort(list2)
