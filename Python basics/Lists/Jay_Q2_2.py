a = int(input())
c = [1,1]
for i in range(1,a-1):
    s = c[i] + c[i-1]
    c.append(s)
print((c[a-1]%10))