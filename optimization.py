d = {}
l=[]
n = int(input('enter no.of expression : '))
for i in range(n):
    left,right = input().split(' ')
    d[left]=right
    l.append(right)
    if i==n-1:
        l1,l2=left,right
print(d)
x = []
for i in d:
    for j in l:
        #print(j)
        if i in j:
            break
    else:
        x.append(i)
print(x)
for i in x:
    del d[i]
x = []
d[left]=right        
print('After dead-code elimination')
for i,j in d.items():
    print(str(i)+' = '+str(j))
for i in d.values():
    c=0
    for k,j in d.items():
        if i==j:
            c+=1
        if c>1:
            #del d[k]
            x.append(k)
for i in x:
    del d[i]
print('After common sub-exp elimination')
for i,j in d.items():
    print(str(i)+' = '+str(j))
#print(d)
