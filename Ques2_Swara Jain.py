# -*- coding: utf-8 -*-

#ques 2
print("give the direction to your robot")
up =input("enter upward value:")
down=input("enter downward value:")
left=input("enter left value:")
right=input("enter right value:")
from math import sqrt
x1=int(up)-int(down)
y1=int(left)-int(right)
dist=int(sqrt((x1*x1)+(y1*y1)))
print(dist)
print(x1 , y1)

