def findlr0(lhs,rhs,lr0):
    for i in range(len(rhs)+1):
        x=lhs+'->'+rhs[:i]+'.'+rhs[i:]
        lr0.append(x)
n = int(input("enter the no of prods : "))
arr=[]
for i in range(n):
    arr.append(input())
    lr0=[]
    for i in range(len(arr)):
        ip = arr[i]
        lhs,rhs = ip.split("->")
        prods = rhs.split("|")
        for prod in prods:
            findlr0(lhs,prod,lr0)
print("LR0 items for given prods")
for i in range(len(lr0)):
    print(i,'->',lr0[i])
