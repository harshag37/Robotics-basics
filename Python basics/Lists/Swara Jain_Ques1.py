password=input("enter the suitable password=")
lower = False
upper = False
digit = False
spcl_chr= False
L = ["$","#","@"]
if len(password)>=6 and len(password)<=12:
    for i in password:
        if (i.islower())==True:
            lower= True
        if (i.isupper())==True:
            upper = True
        if (i.isdigit())==True:
            digit = True
        if i in L:
            spcl_chr=True
    if lower and upper and digit and spcl_chr:
        print("VALID")
    else:
        print("INVALID")
else:
    print("INVALID")
    