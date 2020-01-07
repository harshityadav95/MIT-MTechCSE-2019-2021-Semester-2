# string encryption program
b=input("Enter the string")
#b=inpt.split()
i=0
even=[]
odd=[]
while i<len(b):
    if i%2==0:
        even.append(b[i])
    else:
        odd.append(b[i])
    i=i+1
ver=''.join(even+odd)
print(ver)

