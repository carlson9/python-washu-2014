def fib(n):
    if n <=1:
        return n
    retun fib(n-1) + fib(n-2)

for i in range(40):
    print "{0} : {1}".format(i, fib(i))
