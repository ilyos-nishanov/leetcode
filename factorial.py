# import sys

def factorial1(n):
    n_int = int(n)
    result = 1
    for i in range(1,n_int+1):
        result *=i
    return result



def factorial2(n):
    if n == 1:
        return 1
    else:
        return n*factorial2(n-1)


from time import time
t0=time()
factorial2(900)
t1=time()
factorial1(900)    #print(factorial(sys.argv[1]))
t2=time()
print ('function vers1 takes %f' %(t1-t0))
print ('function vers2 takes %f' %(t2-t1))
