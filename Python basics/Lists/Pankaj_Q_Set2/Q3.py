curr = [10,5,1]
n = len(curr)
ans = 0


inn = int(input())
for i in range(3):
    while (inn>= curr[i]):
        ans = ans+1
        inn = inn - curr[i]

        
print(ans)
