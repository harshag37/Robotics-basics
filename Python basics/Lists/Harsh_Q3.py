# python3
import sys


def compute_min_refills(distance, tank, stops):
    refil=0
    i=0
    times=0
    stops.append(distance)
    while i<len(stops)-1:
        if stops[i+1]-refil>=tank:
            if stops[i]==refil or stops[i+1]-stops[i]>tank:
                return -1
            else:
                refil=stops[i]
                times+=1
        i+=1
    return times

if __name__ == '__main__':
    d=int(input())
    m=int(input())
    n=int(input())
    stops=[]
    for i in range(n):
        x=int(input())
        stops.append(x)
    print(compute_min_refills(d, m, stops))
