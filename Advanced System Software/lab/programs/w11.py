storage=[1,1]
number=int(input("Enter the number of Iterations :"))
while (number):
    total=0
    last_elements=storage[-2:]
    for x in last_elements:
        total+=x
    storage.append(total)
    number=number-1
print(storage)
        
        
