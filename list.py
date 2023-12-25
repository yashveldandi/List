#What are list
"""List is a data  type where we can store multiple item under 1 name.
More techinacally lists act like dynamic(means store as much as you need) arrays which means we can add more
items on the fly"""

#Array vs list
"""1. Fixed vs Dynamic size
#means we use refrencial array in list 
#we not store directly in list take refrence(adress)
2.Convenience-->Hetrogeneous
3.Speed of execution
4.Memory"""

#id
L=[1,2,3]
print(id((L)))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))

print(id(1))
print(id(2))
print(id(3))

#Characteristics of List
"""
1.Ordered
means -->L=[1,2,3]
         L1=[3,2,1]
         L==L1
(answer false means ordered )
2.Changeable/Mutable
3.Hetrogeneous-->means add diff dataype
4.Can have duplicates-->l=[1,2,3,1]
5.are dynamic--->add item it increase its memory
6.can be nested-->list inside listL=[20,30[10,5]]
7. items can be accesed
8.can contain any kind of object in python
9."""

#Creating a list

#Empty list
print([])
#1D list-->single list(Homogeneous list-->means all items are same integers)
print([1,2,3,4,5])
#2D-->hetro (bec first int then list )
print([1,2,3,[4,5]])

#3D list inside list inside list
#Homogenous list it is because single list is used
print([[[1,2]],[[3,4]],[[5,6]]])

#Hetrogenous list--.>diff datatype is used
print(['hello',1,2,True,[1,2],5.6,5+2j])

#Using type conversion
print(list("hello"))

#Accesing Items from a List

#Indexing#access one one item
l=[1,2,[3,4,5]]
print(l[0])
print(l[-1][-2])
print(l[2][0])
print(l[-1])
a=[[[1,2],[3,4]],[[5,6],[7,8]]]
#print(5)
print(a[1][0][0])
#print(3)
print(a[0][1][0])
#Print(2)
print(a[0][0][1])

#Slicing(access more than one item at a time)
b=[1,2,3,4,5,6]
print(b[0:3])
#print(4,5,6)
print(b[-3:])
#1,3,5
print(b[0::2])
print(b[-5:-2:2])
#REverssse a string
print(b[::-1])

#Adding items to a List
#1 append(add 1 item in last)
l1=[1,2,3,4,5]
l1.append(6)
#add in end single item in list [6,7,8]
l1.append([6,7,8])
print(l1)

#extend(add multiple item in list at last)
l1=[1,2,3,4,5]
l1.extend([6,7,8])
print(l1)
#it will break down delhi single char then 
#print into list
l1.extend('delhi')
print(l1)

#insert-->add index which you want
c=[1,2,3,4,5]
c.insert(1,100)
print(c)

#Editing items in a list
#editing with indexing
l=[1,2,3,4,5]
l[-1]=500
print(l)
#with slicing
l[1:4]=[200,300,400]
print(l)


#Deleting items from a list
#del(by using index position)
l=[1,2,3,4,5]
print(l)
del l[-1]
del l[1:3]
print(l)
del l 

#remove(by value of item)
l=[1,2,3,4,5]
l.remove(5)
print(l)

#pop(by index or directly delete last item)
l=[1,2,3,4,5]
l.pop(0)
print(l)
l.pop()
print(l)

#clear--->empty list
l.clear()
print(l)

#operations on list

#Arithmetic(+,*)
#Add two list(concatination or merging)
L1=[1,2,3,4]
L2=[5,6,7,8]
print(L1+L2)
#return 3 times l1
print(L1*3)

#membership
L1=[1,2,3,4,5]
L2=[1,2,3,4,[5,6]]
print(5 in L1)
print(5 not in L1)
#give false bec 5 is not in list is in nested list
print(5 in L2)


#loop
L1=[1,2,3,4,5]
L2=[1,2,3,4,[5,6]]
L3=[[[1,2],[3,4]],[[5,6],[7,8]]]

for i in L1:
    print(i)

for i in L2:
    print(i)

for i in L3:
    print(i)


#List functions
#len/min/max/sorted

#len
L=[2,3,4,5]
print(len(L))
#min
print(min(L))
#max
print(max(L))
#sorted-->defult asceending order
print(sorted(L))
#sorted-->want descending order
print(sorted(L,reverse=True))


#count
L=[1,2,3,1,4,1,5]
print(L.count(1))
#index
print(L.index(2))
#index--it is multiple time it show first occurence
print(L.index(1))

#Reverse
L=[1,2,3,1,4,1,5]
#it permanently reverse the list
L.reverse()
print(L)
print(L)

#sort-->permanent changes(vs sorted-->not make permanent changes)
L=[1,2,3,1,4,1,5]
print(L)
print(sorted(L))
print(L)
L.sort()
print(L)

#Copy-->shallow copy(new adress create same list)
a=[2,1,5,7,0]
b=[2,1,5,7,0]
print(a)
print(id(a))
b=a.copy()
print(b)
print(id(b))

#List comprehension
"""List Comprehension provides a concise way of creating lists.
newlist=[expression for item in iterable if condition==True]
        newlist =[expression for item in iterable if condition == True]


ADVANTAGES OF LIST COMPREHENSION
.More time-efficient and space-efficient than loops
.Require fewer lines of code.
.Transform iterative statement into a formula.

        """
#scalar multiplication on a vector
v=[2,3,4]
s=-3
#x=[]
# for i in v:
#     x.append(i*s)

# print(x)
print([i*s for i in v])

#Add squares
L=[1,2,3,4,5]
print([i**2 for i in L])

#Print all numbers divisible by 5 in the range 1 to 50
print([i for i in range(1,51) if i%5 == 0])


# for i in range(1,51):
#     if i%5 == 0:
#         print(i)

#find languages which start with letter p
languages=['java','python','php','c','javascript']
print([i for i in languages if i.startswith('p')])

#Nested if with list comprehension
basket =['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']
# add new list from my_fruits and items if the fruit exist in basket and also start with 'a'
print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])

#Print(3,3) matrix using list comprehension--> Nested List Comprehenion
print([[i*j for i in range(1,4)] for j in range(1,4)])

#Cartesian product--> List Comprehension on 2 lists together
L1=[1,2,3,4]
L2=[5,6,7,8]
print([i*j for i in L1 for j in L2 ])

#2 way to traverse a list
#. itemwise
L1=[1,3,5,7]
for  i in L1:
    print(i)
#.indexwise
#o position 1 ,1--3,2-->5,3-->7
L1=[1,3,5,7]
for i in range(0,len(L1)):
    print(i)

#by item
L1=[1,3,5,7]
for i in range(0,len(L1)):
    print(L1[i])

#Zip 
"""The zip() function return a zip object,which an iterator of tuples Where the first item in each passed iterator
is paired together, and then the second item in each passed iterator are paired together.

if the passed iterators have different lengths, the iterator with the least items decideds the length of the new iterator."""

#Write a program to add items of 2 lists indexwise
#add l1 and l2 create l3(index wise add item)
L1=[1,2,3,4]
L2=[-1,-2,-3,-4]
list(zip(l1,L2))

print([i+j for i ,j in zip(L1,L2)])

#Store a built in functions in a list
L=[1,2,print,type,input]
print(L)

#Disadvantages of python lists
""".slow
   .Risky usage
   a=[1,2,3]
   b=a
   print(a)
   print(b)

   a.append(4)
   print(a)
   print(b)
   .eats up more memory"""

#Risky usage
#if you change in a automatically change in b for that use copy

a=[1,2,3]
b=a
print(a)
print(b)

a.append(4)
print(a)
print(b)

a=[1,2,3]
b=a.copy()
print(a)
print(b)

a.append(4)
print(a)
print(b)
#lists are mutable