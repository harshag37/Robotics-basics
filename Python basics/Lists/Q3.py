T = int(input())
D = int(input())
L = int(input())
S = input()
S = S.split(" ")
S.append(T)
k = 0
S.insert(0,0)
count = 0
case = 0
for i in range(L):
    if int(S[i+2]) > D + int(S[k]):
        if D + int(S[i+1]) < int(S[i+2]) :
            print(-1)
            case = -1
        if case != -1:
            k = i+1
            count = count + 1
    if case == -1:
        break
if case != -1 :
    print(count)     
