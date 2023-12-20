""" 14/sep/2023
Python Data Types	 """
# x="Hello"
# print(type('x'))
# print(type(12))
# list=[12,"satyam","Rahul",23,897]
# print(list)
# print(list[::-1]) #REVERSE THE STRING   
# print(list[0:3:1])
# user innput list 
# list=[]
# n=int(input("Enter the no of items to store in list: "))
# for l in range(0,n):
#     i=int(input('Enter the items to store in list: '))
#     result=list.append(i)
# print(list)

# Python program to interchange first and last elements in a list
# print(list)
# def swap(l2):
#     size=len(l2)
#     temp=l2[0]
#     l2[0]=l2[size-1]
#     l2[size-1]=temp
#     return l2
# print(swap([12,56,8,'Satyam','kumar',63,'Rahul']))

# Write a python peogram to swap two elements in list
# def swap2(lis2,i1,i2):
#     temp=lis2[i1]
#     lis2[i1]=lis2[i2]
#     lis2[i2]=temp
#     return lis2
# lis2 = [456,645,58,13,4,65,64,63]
# i1=1
# i2=6
# print(swap2(lis2, i1-1, i2-1))

# Maximum of two numbers in Python
# list=[45,65]
# print(max(list))
# a=list[0]
# b=list[1]
# if a>b:
#     print(a)
# else:
#     print(b)

# # Minimum of two numbers in Python
# print(min(list))

# check if element exists in list

# list=[54,645,64,21,9,32,3,5,6,41]
# for i in list:
#     n=int(input('Enter a number to check it is present in list or not: '))
#     if n==i:
#         print("found")
#         break
#     else:
#         print("Not found")
#         break
    
# ways to clear a list in Python
# list=[46,979,6,2,67]
# print(list)
# list.clear()
# print(list)
# list=[]
# print(list)
# list*=0
# print(list)

# Reversing a List
# print(list[::-1])
# list.sort()
# print(list)

# Cloning or Copying a list
# list2=list.copy()
# print(list2)
# def cloning(l):
#     cloned=l[:]
#     return cloned
# l=[45,56,32,64,56]
# print(f'list before cloning {list}')
# print(f"list after cloning {cloning(l)}")    

# # # Use the extend method
# def clone2(l):
#     l_clone=[]
#     l_clone.extend(l)
#     return l_clone
# l=[45,56,32,64,56]
# print(f"list before clone {l}")
# print(f"list after cloned {clone2(l)}")
    
    # Count occurrences of an element in a list
# l=[45,56,33,64,56,45,32]
# y=45
# def occur(l,y):
#     count=0
#     for x in l:
#         if x==y:
#             count+=1
#     return count
# print(f"{y} is occured {occur(l,y)} times")

#    Program to find sum and average of List in Python
# s=sum(l)
# print(s)
# count=0
# for i in l:
#     count+=i
# print(f"sum is {count}")
# print(f"avg is {int(count/2)}")

    # Sum of number digits in List
# l=[45,56,33,64,56,45,32]
# lis=[]
# for ele in l:
#     sum=0
#     for digit in str(ele):
#         sum+=int(digit)
#     lis.append(sum)
# print(l)
# print(lis)
     
     
# test_list = [12, 67, 98, 34]
 
# # printing original list
# print("The original list is : " + str(test_list))   
# res = []
# for ele in test_list:
#     sum = 0
#     for digit in str(ele):
#         sum += int(digit)
#     res.append(sum)
     
# # printing result
# print ("List Integer Summation : " + str(res))

#    Multiply all numbers in the list
# l=[4,5,2]
# mul=1
# for i in l:
#     mul*=i
# print(mul)
    
    
#     # program to find smallest number in a list
# l=[45,56,33,64,56,45,32]

# res=min(l)
# print(res)
# l.sort()
# print(l)
# print(l[0])
    
    # Program to Find Largest Number in a List
    
# print(l[-1])
# print(max(l))

    # program to find second largest number in a list
# print(l[-2])

#    program to print even numbers in a list
# l2=[]
# for i in l:
#     if (i%2)==0:
#         print(i)
#         l2.append(i)
# print(l2)

    # Python program to print odd numbers in a List

# l3=[]
# for i in l:
#     if i%2 !=0:
#         print(i)
#         l3.append(i)
# print(l3)


#    Python program to print all even numbers in a range
# l4=[]
# r1=2
# r2=9
# for i in range(r1,r2):
#     if i%2==0:
#         # print(i)
#         l4.append(i)
# print(l4)

""" Python program to count Even and Odd numbers in a List
  Sample:
  Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

Input: list2 = [12, 14, 95, 3]
Output: Even = 2, odd = 2  """

# li1=[]
# li2=[]
# list=[654,6345,97,3,3,64,4,56,8,48]
# for i in list:
#     if i%2==0:
#         li1.append(i)
#     else:
#         li2.append(i)
# print(li1)
# print(li2)
# print(f"Even = {len(li1)}, odd = {len(li2)}")

""" Python program to print positive and negative numbers in a list
Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]"""

# l=[]
# l1=[]
# list1 = [12, -7, 5, 64, -14]
# for i in list1:
#     if i>=0:
#         l.append(i)
#     else:
#         l1.append(i)
# print(f"Positive numbers = {l}, and Negative numbers = {l1}")
    
    
""" Remove multiple elements from a list in Python 
Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]"""

# r=[]
# nl=[]
# n=int(input("Enter numbers to remove: "))
# li=[12, 15, 3, 10]
# for i in li:
#     if i==n:
#         r.append(i)
#     else:
#         nl.append(i)
# print(f"Remove = {r}, New_list = {nl}")


""" Write a program to remove all even numbers from a list
"""
# list=[45,65,3,41,58,13,56,90]
# for i in list:
#     if i%2==0:
#         list.remove(i)
# print(list)
  
""" Remove empty tuples from a list
Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]

Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”), (),  (”,”),()]
Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]
  """


# tuples = [(), ('ram', '15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (','),()]
# for i in tuples:
#    if len(i)==0:
#        tuples.remove(i)
# print(tuples)


# li=[(',')]
# for x in li:
#     print(len(x))

""" Program to print duplicates from a list of integers
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]"""

# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# p=[]
# d=[]
# for i in list:
#     if i not in p:
#         p.append(i)
#     elif i not in d:
#         d.append(i)
# print(d)

"""  Using the Brute Force approach Python3
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]"""


# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# def duplicate(list):
#     d=[]
#     p=[]
#     for i in list:
#         if i not in p:
#             p.append(i)
#         elif i not in d:
#             d.append(i)
#     return p
# print(duplicate(list))
            
            
""" Remove empty List from List
The original list is : [5, 6, [], 3, [], [], 9]
List after empty list removal : [5, 6, 3, 9]"""


# lis=[5, 6, [], 3, [], [], 9]
# lis1=[]
# empty=[]
# for i in lis:
#     if i:
#         lis1.append(i)
#     else:
#         empty.append(i)
# print(f"Empty = {empty}")
# print(lis1)


""" Convert List to List of dictionaries
Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”] 
Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}] 
Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3. 

Input : test_list = [“Gfg”, 10], key_list = [“name”, “id”] 
Output : [{‘name’: ‘Gfg’, ‘id’: 10}] 
Explanation : Conversion of lists to list of records by keys mapping."""

# test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
# key_list = ['name','id']
# n=len(test_list)
# res=[]
# for i in range(0,n,2):
#     res.append({key_list[0]:test_list[i],key_list[1]:test_list[i+1]})
# print(res)


""" --------------------------------------------------------------------------------------------------------------------- """

""" Python Collections (Arrays)
There are four collection data types in the Python programming language:

1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members. """
        
""" --------------------------------------------------------------------------------------------------------------------- """       
        
        
    
""" Convert Lists of List to Dictionary
The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5, 6]] 
The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}
"""
# og_list=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# dict={}
# for i in og_list:
#     dict[tuple(i[:2])] = tuple(i[2:])
# print(dict)

""" Find Uncommon elements in Lists of List
The original list 1 : [[1, 2], [3, 4], [5, 6]]
The original list 2 : [[3, 4], [5, 7], [1, 2]]
The uncommon of two lists is : [[5, 6], [5, 7]]"""

# list1=[[1, 2], [3, 4], [5, 6]]
# list2=[[3, 4], [5, 7], [1, 2]]
# un_list=[]
# for i in list1:
#     for j in list2:
#         if i not in list2 and j not in list1:
#             un_list.append(i)
#             un_list.append(j)
# print(un_list)

# for i in list1:
#     if i not in list2:
#         un_list.append(i)
# for j in list2:
#     if j not in list1:
#         un_list.append(j)
# print(un_list)



""" Python program to select Random value from list of lists
Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
Output : 7
Explanation : Random number extracted from Matrix."""

# import random
# test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
# # n=[4,5,5]
# x=random.choice(test_list)    //choice() returns a random selected element from the specified sequence or Array
# print(x)


""" Python – Reverse Row sort in Lists of List
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]"""

# list=[[4,1,6],[7,8],[4,10,8]]
# for i in list:
#     i.sort(reverse=True)
# # print(list)
# print(list)


""" Pair elements with Rear element in Matrix Row
The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]"""


# tl=[[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# res=[]
# for i in tl:
#     res.append([[j,i[-1]] for j in i[:-1]])
# print(res)
    
""" -------------------------------------------------------------------------------------------------------------------- """

""" Variables in Python """
# m=30
# n=50
# m=n
# print(m,n)

""" 
1. Camel Case: Second and subsequent words are capitalized, to make word boundaries easier to see.
(Presumably, it struck someone at some point that the capital letters strewn throughout 
the variable name vaguely resemble camel humps.)
Example: numberOfCollegeGraduates
2.Pascal Case: Identical to Camel Case, except the first word is also capitalized.
Example: NumberOfCollegeGraduates
3.Snake Case: Words are separated by underscores.
Example: number_of_college_graduates """


""" Python Control Structures	
Loops and Conditional statements are called Python Control Structures
>> LOOPS: For loops and while loops
>> CONDITIONAL STATEMENTS: if, if-else, if-elif-elif.....else"""

""" LAMBDA Functions
Syntax: lambda arguments : expression
"""
# x=lambda a: a+5
# print(x(2))

# n=lambda o,p : o*p
# print(n(5,6))


""" PYTHON FUNCTIONS
# break and continue Statements, and else Clauses on Loops
1.break: Break statememnt breaks the innermost enclosing for for and while loop.
>> It breaks inner coditional statements

 
"""

# for i in range(2,10):
#     for j in range(2,i):
#         if i%j == 0:
#             print(f"{i} equals {j} * {i//j}")
#             break
#     else:
#             print(f"{i} is a prime nnumber")
        


""" 2. continue: Continues with the next iteration of the loop """
# for n in range(2,10):
#     if n%2==0:
#         print(f"{n} is a Even Number.")
#         # continue
#     else:
#         print(f"{n} is a Odd Number.")
  