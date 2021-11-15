n1 = int(input())
n2 = int(input())
l = []
c = 0
for p in range(1, n1):
    if n1%p == 0:
        if n2%p == 0:
            l.append(p)
        c = max(l)
        
        
   
print(c)
            
     
         
    
        
