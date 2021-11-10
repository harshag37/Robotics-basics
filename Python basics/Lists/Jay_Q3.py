class refills:
    def __init__(self, d, m, n):
        
        self.distance = d
        self.maxdist = m
        self.numofstop = n
        self.refill = 0
        self.sum = 0
        self.stops = []

    def inputs(self):
            d1, d2, d3 ,d4 = input().split()
            self.stops = [int(d1), int(d2), int(d3), int(d4)]

    def findrefill(self):
        
        for i in range(0, self.numofstop):
            if self.maxdist<(self.stops[i]-self.stops[i-1]):
                self.refill = -1
                print(self.refill)
                exit()

            if self.sum>self.maxdist:
                self.sum = self.stops[i-1]
                self.refill += 1

            self.sum = self.sum + self.stops[i]

        print(self.refill)

a = int(input())
b = int(input())
c = int(input())

car = refills(a, b, c)
refills.inputs(car)
refills.findrefill(car)
