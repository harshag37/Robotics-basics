import math

class robot:

    def __init__(self, u, d, l, r):
        self.x = 0 #x coordinate
        self.y = 0 #y coordinate
        self.up = u #distance travelled in up direction
        self.down = d #distance travelled in down direction
        self.left = l #distance travelled in left direction
        self.right = r #distance travelled in right direction

    #function for calulating distance
    def distcal(self):
        if self.up != 0:
            self.x = self.x + self.up
        else:
            self.x = self.x

        if self.down != 0:
            self.x = self.x - self.down
        else:
            self.x = self.x
        
        if self.left != 0:
            self.y = self.y - self.down
        else:
            self.y = self.y

        if self.right != 0:
            self.y = self.y + self.right
        else:
            self.y = self.y

        D = math.sqrt((self.x) ** 2 + (self.y) ** 2) #distance between initial point and final point

        print("The robot travelled {} unit distance".format(D))

#input form users
a = int(input("Up distance: "))
b = int(input("Down distance: "))
c = int(input("Left distance: "))
d = int(input("Right distance: "))

robo1 = robot(a,b,c,d)
robo1.distcal()


