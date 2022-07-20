# magic_square = [[8, 3, 4],
#                 [1, 5, 9],
#                 [6, 7, 2]]
# row1sum=0
# row2sum=0
# row3sum=0
# column=0
# column1=0
# column2=0
# diagona1=0
# diagona2=0
# i=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square[i]):
#         if i==0:
#             row1sum=row1sum+magic_square[i][j]
#         if i==1:
#             row2sum=row2sum+magic_square[i][j]
#         if i==2:
#             row3sum=row3sum+magic_square[i][j]
#         j=j+1
#     i=i+1
# print(row1sum)
# print(row2sum)
# print(row3sum)
# a=0
# while a<len(magic_square):
#     k=0
#     while k<len(magic_square[a]):
#         if k==0:
#             column+=magic_square[a][k]
#         elif k==1:
#             column1+=magic_square[a][k]
#         elif k==2:
#             column2+=magic_square[a][k]
#         k=k+1
#     a=a+1
# print(column)
# print(column1)
# print(column2)
# b=0
# while i<len(magic_square):
#     diagona1+=magic_square[b][b]
#     b+=1
# print(diagona1)
# l=0
# n=2
# while i<len(magic_square):
#     diagona2+=magic_square[l][n]
#     l+=1
#     n-=1
# print(diagona2)
# if row1sum==row2sum==row3sum==column==column1==column2==diagona1==diagona2:
#     print("this is a magic square")
# else:
#     print("not")

# r=int(input("enter the number of rowe:"))
# c=int(input("enter the number of coloum:"))
# magic_square=[]
# print("enter the entries rowwise:")
# for i in range(c):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     magic_square.append(a)
# for i in range(r):
#     for j in range(c):
#         print(magic_square[i][j],end="")
#     print()
