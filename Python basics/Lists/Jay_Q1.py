upper = 0
lower = 0
digit = 0
symbols = 0
pw = input()

if (len(pw)>=6 and len(pw)<=12):
    for i in pw:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isdigit():
            digit += 1
        if i == chr(35) or i == chr(36) or i == chr(64):
            symbols += 1


if (upper>=1 and lower>=1 and digit>=1 and symbols>=1):
    print("VALID")
else:
    print("INVALID")
