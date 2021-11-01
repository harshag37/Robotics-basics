import math

def main():
    up=int(input())
    down=int(input())
    left=int(input())
    right=int(input())

    x=0
    y=0

    x=x+right-left
    y=y+up-down

    ans=math.sqrt(x*x + y*y)

    print(round(ans))


main()