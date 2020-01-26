#digital root
def digitroot(n):

    while(n>9):
        
        s=0
        while(n!=0):
            s=s+n%10
            n=n//10
        if(s>9):
            n=s
        
    return(s)






num=int(input("Enter the number"))
print(digitroot(num))

    
