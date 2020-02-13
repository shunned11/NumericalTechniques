import random 
import math

def derivat(x):
    a=complex(3*x*x-1)
    return a

def poly(x):
    b=complex((x*x*x)-x-1)
    return b

def tang(x):
    ans=complex(x-(poly(x)/derivat(x)))
    return ans

print("The polynomial is x^3-x-1")
for i in range(2):
    x=random.randint(-1000,1000)
    y=random.randint(-1000,1000)
    x0=complex(x,y)
    x1=x0
    count=500
    while(count!=0):
        x1=tang(x0)
        x0=x1
        count=count-1

    print()
    print("The root is",x1)
    if(x1.imag!=0):
        x3=complex(x1.real,-x1.imag)
        print()
        print("The root is",x3)


