#program for text analyser
tex=input("Enter the string")
text=tex.lower()
temp=text.split()
count=0
for i in temp:
    if i in ['a','an','the']:
        count=count+1
print(count)
