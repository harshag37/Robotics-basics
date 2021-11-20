n1 = int(input())
n2 = int(input()) 
l = min(n1,n2)
c = 0
for p in range(1, l+1):
    if n1%p == 0 and n2%p == 0:
        c = p
        
print(c)
         
    
        
