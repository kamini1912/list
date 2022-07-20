
a=[1,2,3,-1,3,-4,-2,2,0]
i=0
b=0
list=[]
while i<len(a):
    if a[i]<0:
        list.append(0)
    else:
        list.append(a[i])
    i+=1
print(list)

