from math import sqrt

up = int(input("UP "))
down = int(input("DOWN "))
left = int(input("LEFT "))
right = int(input("RIGHT "))

x_dist = 0 + right - left
y_dist = 0 + up - down

print(int(sqrt(x_dist*x_dist + y_dist*y_dist )))