n1 = int(input())
n2 = int(input())
t = 0
for p in range(2, n1):
    if n1%p == 0:
        if n2%p == 0:
            t+=1
            print(p)
            break
if t == 0:
    print("1")
         
         
    
        