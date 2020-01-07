#perfect number program
i=1
while i<10001:
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if i==sum:
        print(i)
    i=i+1
