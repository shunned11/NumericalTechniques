import random
import math

a=float(input("Enter value of a "))
b=float(input("Enter value of b "))
c=float(input("Enter value of c "))
d=float(input("Enter value of d "))

def poly(a,b,c,d,x):
    v=float((a*x*x*x)+(b*x*x)+c*x+d)
    return v

def sec(a,b,c,d):
    t1=random.randint(-1000,1000)
    t2=random.randint(-1000,1000)
    num=float(poly(a,b,c,d,t2)*(t2-t1))
    den=float(poly(a,b,c,d,t2)-poly(a,b,c,d,t1))
    t3=float(t2-num/den)
    count=0

    while(abs(poly(a,b,c,d,t3))>=0.0001):
        if(abs(poly(a,b,c,d,t2))<abs(poly(a,b,c,d,t1))):
            t1=float(t2)
        num=float(poly(a,b,c,d,t2)*(t2-t1))
        den=float(poly(a,b,c,d,t2)-poly(a,b,c,d,t1))
        t3=float(t2-num/den)
        count=count+1
    print("The root is",t3)
    print("Number of iterations",count)

sec(a,b,c,d)

