#ques 2

print("give the direction to your robot")

from math import sqrt
for i in range(1,5):
  if i<=5:
    direction = input("enter the direction=")
    direction = direction.lower()
    if direction == "up":
        up=input("enter the value for up=")
    if direction == "down":
        down=input("enter the value for down=")
    if direction == "left":
        left=input("enter the value for left=")
    if direction == "right":
        right=input("entr the value for right=")
x1=int(up)-int(down)
y1=int(left)-int(right)
dist=int(sqrt((x1*x1)+(y1*y1)))
print(dist)
print(x1 , y1)