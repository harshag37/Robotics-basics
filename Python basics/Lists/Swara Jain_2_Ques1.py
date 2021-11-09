num=input()
num=num.split()
i=0
a=int(num[0])
b=int(num[1])
for x in range(min(a,b)):
    if b != 0:
        i=a
        a=b
        b=i%b
print(a)