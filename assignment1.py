b=ord('A')
n=11
for i in range(n):
    for j in range(i+1):
        f=0
        if(j==i):
            print(chr(b+i),end="")
        else:
            print(" ",end="")
    for k in range(i+2,n):
        print(" ",end="")
    for l in range(i+1,n):
        f=1
        print(" ",end="")
    if(f==1):
        print(chr(b+i),end="")
    print()

for i in range(n,0,-1):
    for j in range(0,i-2):
        print(" ",end="")
    if(b+i-2>=65):
        print(chr(b+i-2),end="")
    for k in range(n+1,i,-1):
        print(" ",end="")
    for l in range(n,i,-1):
        print(" ",end="")
    if(b+i-2>=65):
        print(chr(b+i-2),end="")
    print()



