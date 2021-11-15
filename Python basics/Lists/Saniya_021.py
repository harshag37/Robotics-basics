n = int(input())
t = 0
l = [0,1]
for i in range(2, n+1):
    if i == 2:
        l.append(1)
    if n > 1:
        l[i] = l[i-1] + l[i-2]
        l.append(l[i])
    if i == n:
        t = l[i] % 10
    
    
print(t)


