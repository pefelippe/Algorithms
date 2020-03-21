import random

def Swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux

def Mergesort(v):
	mergesort(v, 0, len(v) - 1)
	print(v)
def mergesort(v, i, n):
	if (i >= n): return

	k = (i + n) / 2 	# elemento central

	mergesort(v, i, k)
	mergesort(v, k+1, n)

	Intercalacao(v, i, k, n)

def Intercalacao(v, i, meio, fim):

	inicio = i
	inicio2 = meio + 1

	if (v[meio] <= v[inicio2]): 
		return

	while (inicio <= meio and inicio2 <= fim):

		if (v[inicio] <= v[inicio2]): 
			inicio +=1

		else:
			valor = v[inicio2]
			index = inicio2

			while (index != inicio):
				v[index] = v[index - 1]
				index -= 1

			v[inicio] = valor

	inicio += 1
	meio += 1
	inicio2 += 1



# Main

list = []

for x in range(20):
	list.append(random.randint(1, 10000))

list2 = [10, 133, 1313, 41, 23, 0, 2, 3 , 100]

Mergesort(list)