text1=input("Enter the Username :")
text2=input("Enter the password :")
d={"username":"password",
   "abc":"cba",
    "123":"321",
    "four":"4",
    "five":"5",
     "six":"6",
    "seven":"7",
    }
if text1 in d:
    print("Username found")
    if text2==d[text1]:
        print("Logged In")
    else:
        print("password mismatch")
else:
    print("Invalid user")
