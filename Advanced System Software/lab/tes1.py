class analyzer:
    def __init__(self,l):
        count=0
        for i in a:
            count+=1
        print("Number of Words:",count)

    def two(l):
        count3=0
        for i in a:
            if(len(i)==2):
                count3+=1
        print("Number of 2-letter words:",count3)

    def start(v):
        count2=0
        for i in a:
            for j in i:
                if(j==v):
                    count2+=1
                break
        print("Number of words Starting with t:",count2)
        
        
        

       
    
a=["today","is","the","test","for","the","lab","subject"]
r=analyzer(a)
v='s'
r=analyzer.start(v)
r=analyzer.two(a)
#star=a.startwith('t')
#print(star)

    
