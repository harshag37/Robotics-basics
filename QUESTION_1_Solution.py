s = input()
numeric = False
small_Alpha = False
caps_Alpha = False
symbol = False


if s.__len__() <= 12 and s.__len__() >= 6 :
    print(s)
    for x in s:
        if  x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9':
            numeric = True


        for i in range(65,90):
            if x == chr(i):
                caps_Alpha = True


        for j in range(97,122):
            if x == chr(j):
                small_Alpha = True



        if  x == '$' or x == '#' or x == '@':
            symbol = True


if numeric == True and small_Alpha == True and caps_Alpha == True and symbol == True:
    print("VALID ")
else:
    print("INVALID")
