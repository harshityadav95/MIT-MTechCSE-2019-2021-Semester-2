# Fibonacci Program
n=int(input("Enter the Number"))
fib=[1,1]
i=1;
while i<n:
    for i in range(2,n+1):
        fib[i]=fib[i]+fib[i-1]
        print(i,end='')
