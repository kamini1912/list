
# a=[[4,3,2],[5,6,7],[9,10,12]]
# i=0
# sum=0
# z=2
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if(i==0):
#             sum=sum+a[i][j]
#         else:
#             sum=sum+a[i][z]
#             break
#         j=j+1
#     i=i+1
# print(sum)


# a=[[5,6,9],8,[6,9,2],4,[10,1,3]]
# i=0
# z=0
# b=[]
# while i<len(a):
#     if(type(a[i]) is not list):
#         x=i-1
#         a[x].insert(j,(a[i]))
#     else:
#         j=0
#         while j<len(a[i]):
#             j+=1
#     i+=1
# print(a)



# n=int(input("enter the number "))
# count=0
# i=1
# b=[]
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i=i+1
# b.append(n)
# if count==2:
#     print(b,"prime")
# else:
#     print(b,"not prime") 



# a=[2000,300,5000,500,110,100,10]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]//=10
#     i=i+1
# print(b)




# l=[1,1,2,3,4,5,1,2,]
# i=0
# b=[]
# while i<len(l):
#     j=l[i]
#     if i not in l:
#         b.append(j)
#     i=i+1
# print(b)



# n=int(input("enter the number"))
# i=0
# while i<n:
#     sum=n%10
#     b=n-sum
#     i=i+1
# print(b,"+",sum)


# a=[6,7,8,0,8,3,2,0]
# i=0
# b=[]
# while i<len(a):
#   if a[i]==0:
#     b.append(1)
#   else:
#     b.append(a[i])  
#   i+=1
# print(b)  




# binary_number=[1,0,0,1,1,0,1,1,]
# i=0
# sum=0
# while i<len(binary_number):
#     a=binary_number[-i-1]
#     sum=sum+a*(2**i)
#     i=i+1
#     print(sum)



# i=0
# b=[]
# c=[]
# sum=0
# while i<5:
#     n=int(input("enter the number"))
#     sum=sum+n
#     b.append(n)
#     c.append(sum)
#     i=i+1
# print(b)
# print(c)



# a=["usha",21,"kamini",45]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     if type(a[i])==int:
#         c.append(a[i])
#     i=i+1
# print(b)
# print(c)
    


# a=[5,1,2,1,3,1]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==k:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(c+b)



# a=[1,0,2,0,3]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(c+b)



# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# prod=1
# while i<len(a):
#     if a[i]<=5:
#         sum=sum+a[i]
#     else:
#         prod=prod*a[i]
#     i=i+1
# print(sum)
# print(prod)


# a=[1,2,0,3,5,0,4,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=0 and a[i]!=5:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=["kamini"]
# i=0
# while i<len(a):
#     j=1
#     while j<len(a[i])+1:
#        print(a[i][-j],end=",")
#        j=j+1
#     i=i+1

# a=[1,2,0,3,5,0,4,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         b.append("k")
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)



# a=[1,2,3,4,1,1,5,6,7,8,6,7]
# i=0
# b=[]
# while i<len(a):
#     j=i+1
#     count=1
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1 
#         j+=1
#     if a[i] not in b:
#         b.append(count)
#     i=i+1
# print(b)

        



# i=0
# b=[]
# c=[]
# sum=0
# while i<5:
#     n=int(input("enter the number"))
#     sum=sum+n
#     b.append(n)
#     c.append(sum)
#     i=i+1
# print(b)
# print(c)


