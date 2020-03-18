

def insertionSort (lista):
	i = 0
	j = 1

	while(i < len(lista) - 1):
		p = i 
		l = j

		while (p >= 0 and lista[p] > lista[l]):
			swap(lista, p, l)
			p-=1
			l-=1
		i+=1
		j+=1

	print("Insertion Sort:", lista)

# Complexity
# O(n)  - best case
# O(n²) - worst case
