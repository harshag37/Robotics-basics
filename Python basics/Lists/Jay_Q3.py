class refills:
    def __init__(self, d, m, n):
        self.i = 0
        self.distance = d
        self.maxdist = m
        self.numofstop = n
        self.refill = 0
        self.sum = 0
        self.stops = []

    def inputs(self):
        for x in range(0, self.numofstop):
            d = int(input())
            self.stops.append(d)

    def findrefill(self):

        for self.i in (0, self.numofstop):
            if ((self.maxdist - self.stops[self.i])<(self.stops[self.i+1]-self.stops[self.i])):
                self.refill += 1
            else:
                self.refill = self.refill

        print(self.refill)

a = int(input())
b = int(input())
c = int(input())



car = refills(a, b, c)
refills.inputs(car)
refills.findrefill(car)




