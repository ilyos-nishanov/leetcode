import sys
from time import time

#brute force
def fib_bf(n):
    n_int = int(n)
    if n_int ==0 :
        return 0
    elif n_int ==1:
        return 1
    else:
        return fib_bf(n_int-1)+fib_bf(n_int-2)
    


#with memoization
def fib_wm(n, memo ={}):
    n_int = int(n)
    if n_int in memo:
        return memo[n_int]
    if n_int <=2:
        return 1
    memo[n_int]= fib_wm(n_int-1,memo)+fib_wm(n_int-2,memo)
    return memo[n_int]

# t0=time()
# print(fib_bf(sys.argv[1]))
t1=time()
print(fib_wm(sys.argv[1]))
t2=time()
# print ('function vers1 takes %f' %(t1-t0))
print ('function vers2 takes %f' %(t2-t1))