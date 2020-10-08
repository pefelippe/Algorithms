def fib(num):
    if(num<=1):
            return num
    return fib(num-2) + fib(num-1)

# T(n) = 2T(n-1) + 1
# By Master Teorem: O(N^2)