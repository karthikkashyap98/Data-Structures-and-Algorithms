'''
recursion is done on the past 2 values of n 

'''


def Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1 
    return Fib(n-1) + Fib(n-2)      

print(Fib(6))

