import sys
def fib(n):
    n_int = int(n)
    if n_int ==0 :
        return 0
    elif n_int ==1:
        return 1
    else:
        return fib(n_int-1)+fib(n_int-2)
    
print(fib(sys.argv[1]))