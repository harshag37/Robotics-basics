password = input()
Cap = False
Sma = False
Digit = False
Special = False
L = ["$","#","@"]
for ele in password:
    if ele.isupper():
        Cap = True
        continue
    if ele.islower():
        Sma = True
        continue
    if ele.isdigit():
        Digit = True
        continue
    if ele in L:
        Special = True
        continue
if len(password) < 6 or len(password) > 12:
    print("INVALID")
elif Cap and Sma and Digit and Special:
    print("VALID")
else:
    print("INVALID")
