#Q1 
password = input("enter your password ")

upper_letter= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num_value =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spl_char  = ["@", "#", "$"]
upper_letter_count =0
lower_letter_count =0
num_value_count =0
spl_char_count =0

if len(password) >=6 and len(password) <=12:
    for i  in password:
         if i in upper_letter:
            upper_letter_count += 1
         if i in lower_letter: 
            lower_letter_count += 1
         if i in num_value:
            num_value_count =+ 1
         if i in spl_char: 
            spl_char_count += 1

if upper_letter_count !=0 and lower_letter_count!=0 and num_value_count!=0 and spl_char_count !=0:
    print ("VALID")
else:
    print("INVALID")





