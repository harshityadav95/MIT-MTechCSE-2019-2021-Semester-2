# Program strig manipulation in python
n=input("Enter the String :")
print("Length of the string is :",len(n))
print("String repeated 10 times :",n*10)
print("First Character of the string is :",n[0])
print("First three character of the string:",n[0:3])
print("Last three character of the string :",n[len(n)-3:])
print("String in reverse",n[::-1])

if(len(n)<7):
    print("string to small")
else:
    print("seventh char is :",n[6])
    
print("String with first and last character removed",n[1:len(n)-1])
print("String in upper case",n.upper())
for i in n:
    print(end='')
print("End of Program ")
