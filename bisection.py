import random
a=float(input("Enter value of a "))
b=float(input("Enter value of b "))
c=float(input("Enter value of c "))
print()
print("The polynomial is",a,"x^2+",b,"x+",c)
def poly(a,b,c,x):   
    v=float((a*x*x)+(b*x)+c)
    return v

def ab(a,b,c):
    for i in range(2):
        count=0
        aint=1.0
        while(aint>0.0):
            #ax=float(input("Enter value for which f(x) is -ve "))
            ax=random.randint(-1000,1000)
            aint=poly(a,b,c,ax)
            count=count+1
        bint=-1.0
        while(bint<0.0):
            #bx=float(input("Enter value for which f(x) is +ve "))
            bx=random.randint(-1000,1000)
            bint=poly(a,b,c,bx)
            count=count+1
        
        cint=float((ax+bx)/2)
        while(poly(a,b,c,cint)!=0.0):
            if(poly(a,b,c,cint)>0):
                bx=cint
            if(poly(a,b,c,cint)<0):
                ax=cint
            cint=float((ax+bx)/2.0)
            count=count+1
            
        print("The root is=", cint)
        print("The number of iteration required are",count)
        print()

ab(a,b,c)