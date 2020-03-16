def swap(v, i, j):
	aux = v[i]
	v[i] = v[j]
	v[j] = aux

# - ShellSort -

def ShellSort(V):  
	h = len(V)/2 

	while (h > 0):
		i = 0
		while (i+h < len(V)):
			if(V[i] > V[i+h]):
				swap(V, i, i+h)
			i+=1 
		h-=1 	# nessa versao do shellsort, o salto diminui em 1 a cada loop.

	print('Lista Ordenada [ShellSort] =  {} '.format(V))
