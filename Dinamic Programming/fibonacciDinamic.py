def fib(N):
    list = []
    
    if (N>=0):
        list.append(0)

    if(N>=1):
        list.append(1)

    i=2

    while (i<=N):
        list.append(list[i-2] + list[i-1])
        i+=1

    return list

N = int(input("N: "))
fib = fib(N)
print(fib)


# O(n)

