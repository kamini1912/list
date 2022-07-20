

# n=int(input("enter the number"))
# i=0
# b=[]
# sum=0
# while i<n:
#     num=int(input("enter the number"))
#     sum=sum+n
#     b.append(n)
#     i=i+1
# print(sum)


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] 
# i=0
# b=[]
# while i<len(a):
#     if a[i]<=5:
#         b.append(a[i])
#     elif a[i]>6:
#         b.append(i*i)
#     i=i+1
# print(b[6:30])


# a=[1,0,4,0,2,0,5]
# b=[]
# for i in a:
#     b.append(i)
#     a.append(i)
# print(b+b)


# i=0
# b=[]
# sum=0
# while i<5:
#     n=int(input("enter the number"))
#     sum=sum+n
#     b.append(sum)
#     i=i+1
# print(b)

# a=[1,1,2,3,4,5,1,2]
# i=0
# b=[]
# while i<len(a):
#     j=a[i]
#     if i not in b:
#         b.append(j)
#     i=i+1
# print(b)

# def printmax(x,y):
#     if  x>y:
#         print(x)
#     elif x==y:
#         print("equal")
#     else:
#         print(y)
# printmax(5,9)

# a="2"
# b="2"
# print(a+b)

# def fun ():
#     x=100
#     print(x)
# x=1
# fun()

# x=0
# while x>20:
#     x=x+3
# print(x)\



# List = ['G', 'E', 'E', 'K', 'S', 'F',
#         'O', 'R', 'G', 'E', 'E', 'K', 'S']
# print("Initial List: ")
# print(List)
 


# Sliced_List = List[3:8]
# print("\nSlicing elements in a range 3-8: ")
# print(Sliced_List)

# liced_List = List[5:]
# print("\nElements sliced from 5th "
#       "element till the end: ")
# print(Sliced_List)

# liced_List = List[:]
# print("\nPrinting all elements using slice operation: ")
# print(Sliced_List)




 
# Creating a List
# List = []
# print("Blank List: ")
# print(List)
 
# # Creating a List of numbers
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)
 
# # Creating a List of strings and accessing
# # using index
# List = ["Geeks", "For", "Geeks"]
# print("\nList Items: ")
# print(List[0])
# print(List[2])
 
# # Creating a Multi-Dimensional List
# # (By Nesting a list inside a List)
# List = [['Geeks', 'For'], ['Geeks']]
# print("\nMulti-Dimensional List: ")
# print(List)



# Creating a List with
# the use of Numbers
# (Having duplicate values)
# List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(List)
 
# Creating a List with
# mixed type of values
# (Having numbers and strings)
# List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# print("\nList with the use of Mixed Values: ")
# print(List)


# list1 = []
# print(len(List1))
 
# # Creating a List of numbers
# List2 = [10, 20, 14]
# print(len(List2))


# Python program to demonstrate
# Addition of elements in a List
 
# Creating a List
# List = []
# print("Initial blank List: ")
# print(List)
 
# # Addition of Elements
# # in the List
# List.append(1)
# List.append(2)
# List.append(4)
# print("\nList after Addition of Three elements: ")
# print(List)
 
# # Adding elements to the List
# # using Iterator
# for i in range(1, 4):
#     List.append(i)
# print("\nList after Addition of elements from 1-3: ")
# print(List)
 
# # Adding Tuples to the List
# List.append((5, 6))
# print("\nList after Addition of a Tuple: ")
# print(List)
 
# # Addition of List to a List
# List2 = ['For', 'Geeks']
# List.append(List2)
# print("\nList after Addition of a List: ")
# print(List)



# Python program to demonstrate
# Addition of elements in a List
  
# Creating a List
# List = [1,2,3,4]
# print("Initial List: ")
# print(List)
 
# # Addition of Element at
# # specific Position
# # (using Insert Method)
# List.insert(3, 12)
# List.insert(0, 'Geeks')
# print("\nList after performing Insert Operation: ")
# print(List)

# # Creating a List with
# # the use of multiple values
# List = ["Geeks", "For", "Geeks"]
 
# # accessing a element from the
# # list using index number
# print("Accessing a element from the list")
# print(List[0])
# print(List[2])
 
# # Creating a Multi-Dimensional List
# # (By Nesting a list inside a List)
# List = [['Geeks', 'For'], ['Geeks']]
 
# # accessing an element from the
# # Multi-Dimensional List using
# # index number
# print("Accessing a element from a Multi-Dimensional list")
# print(List[0][1])
# print(List[1][0])




# # Python program to demonstrate
# # Removal of elements in a List
 
# # Creating a List
# List = [1, 2, 3, 4, 5, 6,
#         7, 8, 9, 10, 11, 12]
# print("Initial List: ")
# print(List)
 
# # Removing elements from List
# # using Remove() method
# List.remove(5)
# List.remove(6)
# print("\nList after Removal of two elements: ")
# print(List)
 
# # Removing elements from List
# # using iterator method
# for i in range(1, 5):
#     List.remove(i)
# print("\nList after Removi")

# Creating a List
# List = ['G', 'E', 'E', 'K', 'S', 'F',
#         'O', 'R', 'G', 'E', 'E', 'K', 'S']
# print("Initial List: ")
# print(List)
 
# # Print elements from beginning
# # to a pre-defined point using Slice
# Sliced_List = List[:-6]
# print("\nElements sliced till 6th element from last: ")
# print(Sliced_List)
 
# # Print elements of a range
# # using negative index List slicing
# Sliced_List = List[-6:-1]
# print("\nElements sliced from index -6 to -1")
# print(Sliced_List)
 
# # Printing elements in reverse
# # using Slice operation
# Sliced_List = List[::-1]
# print("\nPrinting List in reverse: ")
# print(Sliced_List)
 

# below list contains square of all
# odd numbers from range 1 to 10
# odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
# print(odd_square)

# b = []
# for x in range(1, 11):
#     if x % 2 == 1:
#        b.append(x**2)
# print(b)

# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     s=sum(a[i][:])
#     i+=1
#     print(s)

# [[1,2,3],[4,5,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     s=sum(a[i][:])
#     i+=1
#     print(s)

# a=['Ricky Rivera', 98, 'Math', 90, 'Science']
# a.remove("")
# print(a)
	






       
        























