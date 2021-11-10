a, b = input().split()
c = []
d = []
for i in range(1,int(a)):
    if (int(a)%i) == 0:
        c.append(i)
for j in range(1,int(b)):
    if (int(b)%j) == 0:
        d.append(j)
e = []
for k in c:
    for l in d:
        if k == l:
            e.append(k)

print(max(e))
