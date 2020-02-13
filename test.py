#print("Hello World")
a=2
b=3
#print(a+b)
#print("Hellow World",a+b)
for i in range(5,0,-1):
    for j in range(i):
        print(" ", end="")
    for k in range(6-i):
        print("*", end="")
    print("")


for i in range(1,11):
    for j in range(1,11):
        x=0 
        product=i*j
        while(product!=0):
            d=product%10
            product=product/10
            x=x+1
        if x==0:
            print(" "+product)
        else:
            print(product)

            print("")