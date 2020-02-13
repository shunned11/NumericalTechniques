a=int(input("Enter integer "))
b=int(input("Enter integer "))
def hcf1(a,b):
    for x in range(1,min(a,b)+1):
        if(a%x==0 and b%x==0):
            gcd=x
    print("HCF=",gcd)

def lcm1(a,b):
    m=max(a,b)
    while(1):
        if(m%a==0 and m%b==0):
            l=m
            print("LCM=",l)
            break
        else:
            m=m+1 

hcf1(a,b)
lcm1(a,b)



        


