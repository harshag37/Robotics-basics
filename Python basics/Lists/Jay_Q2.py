import math

class robot:

    def __init__(self):
        self.x = 0 #x coordinate
        self.y = 0 #y coordinate
        self.up = 0 #distance travelled in up direction
        self.down = 0 #distance travelled in down direction
        self.left = 0 #distance travelled in left direction
        self.right = 0 #distance travelled in right direction
        

    def inputs(self):
        for z in range(0,4):
            m, n = input("Enter Direction and steps:").split()
            m = m.upper()
            n = int(n)
            if m == "UP":
                self.up += n

            elif m == "DOWN":
                self.down += n

            elif m == "LEFT":
                self.left += n

            elif m == "RIGHT":
                self.right += n

            else:
                print("Please enter correct direction.")
                quit()



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

        D = int(math.sqrt((self.x) ** 2 + (self.y) ** 2)) #distance between initial point and final point

        print("The robot is at {} unit distance.".format(D))

robo1 = robot()
robo1.inputs()
robo1.distcal()


