import sys
from time import time

#with list
def factorial1(n):
    n_int = int(n)
    result = 1
    for i in range(1,n_int+1):
        result *=i
    return result


#with recursive function
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n*factorial2(n-1)


#with memoization
def factorial3(n,memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    else:
        memo[n]= n*factorial3(n-1)
        return memo[n]


t0=time()
print(factorial1(900))
t1=time()
print(factorial2(900))    #print(factorial(sys.argv[1]))
t2=time()
print(factorial3(900))    #print(factorial(sys.argv[1]))
t3=time()
print ('function vers1 takes %f' %(t1-t0))
print ('function vers2 takes %f' %(t2-t1))
print ('function vers3 takes %f' %(t3-t2))