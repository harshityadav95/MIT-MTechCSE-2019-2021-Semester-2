text=input("Enter the date in dd/mm/yy :")
a=text.split('/')
d={1:"January",
   2:"feb",
   3:"march",
   4:"april",
   5:"May",
   6:"June",
   7:"July",
   8:"August",
   9:"Sept",
   10:"oct",
   11:"nov",
   12:"Dec"}
print(d[int(a[1])]+" "+a[0]+","+"19"+a[2])
