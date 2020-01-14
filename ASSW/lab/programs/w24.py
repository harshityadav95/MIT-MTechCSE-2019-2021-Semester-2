file=open("text.txt",'r')
file2=open("text2.txt",'w')
l=[]
for i in file:
    r=i.split()
    print(r)
    file2.write(r[0].capitalize()+" "+r[1].capitalize()+" "+r[2]+" "+"301-"+r[3]+"\n")
file.close()
file2.close()
    

 
    
