import math
a=[]
b=[]
c=[]
d=[]
for x in range(3):
    print()
    print("Equation Number",x+1)
    a.append(int(input("Enter coeffecients of x=")))
    b.append(int(input("Enter coeffecients of y=")))
    c.append(int(input("Enter coeffecients of z=")))
    d.append(int(input("Enter coeffecients of constants=")))

def sol(x,y,z):
    count=0
    while True:
        x=(d[0]-b[0]*y-c[0]*z)/a[0]
        y=(d[1]-a[1]*x-c[1]*z)/b[1]
        z=(d[2]-a[2]*x-b[2]*y)/c[2]
        count=count+1
        if math.fabs(a[0]*x+b[0]*y+c[0]*z-d[0])<=0.000000000001:
            break
    print()
    print("X=",x)
    print("Y=",y)
    print("Z=",z)
    print(count)
sol(0,0,0)
