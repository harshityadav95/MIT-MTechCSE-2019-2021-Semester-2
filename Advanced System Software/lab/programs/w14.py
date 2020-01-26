# Email address program
n=int(input("Enter the number of email address :"))
flag=0
for i in range(0,n):
    email=input("Enter the emaill address :")
    b=email.split('@')
    d=b[1].split('.')
    if d[0]=="prof":
        flag=1
if flag==0:
    print("All students:")
else:
    print("Professor detcted :")
    
    
