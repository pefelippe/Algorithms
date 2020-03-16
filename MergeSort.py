
def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux


def MergeSort(lista):
	print('Lista Ordenada [Mergesort] =  {} '.format(merge(lista, 0, len(lista)-1)))

def merge(lista, posIni, posFinal):

	if (posIni == posFinal):
		list1 = []
		list1.append(lista[posIni])
		return list1
	
	k = (posIni + posFinal)/2 

	lista1 = []
	lista2 = []

	lista1.extend(merge(lista, posIni, k))
	lista2.extend(merge(lista, k+1, posFinal))

	return intercalar(lista1, lista2)
	 
def intercalar(v1, v2): # usando na mao mesmo mas n funciona
	
	lista_aux = []
	i = 0
	k = 0

	while ((i <= len(v1) - 1) and (k <= len(v2) - 1)):
		
		if(v1[i] < v2[k]):
			lista_aux.append(v1[i])
			i+=1

		else:
			lista_aux.append(v2[k])
			k+=1

	# caso as listas sejam diferentes em tamanho:	
	while (i <= len(v1) - 1):
		lista_aux.append(v1[i])
		i+=1

	while (k <= len(v2) - 1):

		lista_aux.append(v2[k])
		k+=1

	return lista_aux
