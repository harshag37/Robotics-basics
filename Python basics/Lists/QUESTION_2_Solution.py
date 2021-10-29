from math import sqrt

x = 0
y = 0
up = 0
down = 0
left = 0
right = 0

for x in range(0,4):
    m, n = map(str,input().split())
    query = m.lower()
    if "up" in query:
     up = up +  int(n)
    if "down" in query:
     down = down + int(n)
    if "left" in query:
     left = left + int(n)
    if "right" in query:
     right = right + int(n)

x_dist = 0 + right - left
y_dist = 0 + up - down

print(int(sqrt(x_dist*x_dist + y_dist*y_dist )))