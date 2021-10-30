password = input()

upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["@", "#", "$"]

char = len(password)

upper_count = 0
lower_count = 0
digit_count = 0
symbol = 0
for i in password:
    if char >= 6 and char <= 12:
        if i in upper_case:
            upper_count += 1
        if i in lower_case: 
            lower_count += 1
        if i in digits:
            digit_count += 1
        if i in symbols: 
            symbol += 1


if upper_count > 0 and lower_count>0 and digit_count> 0 and symbol> 0: 
    print("Valid")
else:
     print("invalid")