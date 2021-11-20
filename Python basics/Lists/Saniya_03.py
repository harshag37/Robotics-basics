n = int(input())
l = [1, 5, 10]
t = 0
c = n
while c >= 10:
    c = c - 10
    t+=1
while c >= 5:
    c = c - 5
    t+=1
while c < 10 & c > 5:
    c = c - 5
    t+=1
while c > 1 & c < 5:
    c = c - 1
    t+=1
while c == 1:
    c = c - 1
    t+=1
    

print(t)

