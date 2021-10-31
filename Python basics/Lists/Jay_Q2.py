import math

class robot:

    def __init__(self):
        self.x = 0 #x coordinate
        self.y = 0 #y coordinate
        
    def inputs(self):
        for z in range(0,4):
            m, n = input().split()
            n = int(n)
            if m == "UP":
                self.y += n
            elif m == "DOWN":
                self.y -= n
            elif m == "LEFT":
                self.x -= n
            elif m == "RIGHT":
                self.x += n

    #function for calulating distance
    def distcal(self):
        D = int(0.5*((self.x) ** 2 + (self.y) ** 2)) #distance between initial point and final point
        print(D)

robo1 = robot()
robo1.inputs()
robo1.distcal()


