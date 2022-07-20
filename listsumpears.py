
# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     s=sum(a[i][:2])
#     i+=1
#     print(s)

# a=[[4,3,2],[5,6,7],[9,10,12]]
# i=0
# b=[]
# while i<len(a):
#     s=sum(a[i][0:-1])
#     i=i+1
#     print(s)

# a=[[4,3,2],[5,6,7],[9,10,12]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][-1-j]
#         j=j+1
#     i=i+1
#     print(sum)

 
a=[[5,6,9],8,[6,9,2],4,[10,1,3]]
i=0
z=0
b=[]
while i<len(a):
    if(type(a[i]) is not list):
        x=i-1
        a[x].insert(j,(a[i]))
    else:
        j=0
        while j<len(a[i]):
            j+=1
    i+=1
print(a)
    
	
 
