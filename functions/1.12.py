def fib (n):
    if n==0 or n==1:
        return 0
    else:
        return (n-2)+fib(n-1)
print(fib(6))