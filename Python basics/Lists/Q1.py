A = 0
a = 0
n = 0
s = 0
p = input('Enter your password:')
if (len(p) >= 6 & len(p) <= 12):
    for i in p:
        if i.isupper():
            A += 1
        if i.islower():
            a += 1
        if i.isdigit():
            n += 1
        if i == '@' or i == '#' or i == '$':
            s += 1
        
    if (A>=1 & a>=1 & n>=1 & s>=1):
        print("VALID PASSWORD")

    else:
        print("INVALID PASSWORD")
