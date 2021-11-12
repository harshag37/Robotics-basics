n=int(input())
f=[0,1]
for i in range(1,n+1):
    f[i]=f[i-1]+f[i-2]
    x=f[i]
    f.append(x)
r=f[i]%10
print(r)
