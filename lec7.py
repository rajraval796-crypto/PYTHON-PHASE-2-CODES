#--------------------------------------- code 1 --------------------------------------------------

# s={10,20,22,-22,1,1,10,-22,"RAJ"}
# print(s)
# s.add(-880)
# print(s)
# s.remove("RAJ")
# print(s)
# z=frozenset(s)
# print(type(z))
# # z.add(20)
# x={10,20,-22}
# print(x.issubset(s))
# print(s.issubset(x))
# print(s.issuperset(x))
# print(x.issuperset(s))

#--------------------------------------- code 2 --------------------------------------------------

# x={1,2,3,-1000,"RAJ",88,"RAVAL"}
# y={"raj",2,3,4,-1000,55,88,"RAVAL"}
# x.difference(y) # gives output in form of x-y
# y.difference(x) # gives output in form of y-x
# x.union(y) # gives all the output , and returns the duplicate values only once
# x.intersection(y) # gives output for all the common elements 
# y.symmetric_difference(x) # gives everything except the common elements 

#--------------------------------------- code 3 --------------------------------------------------
# from functools import *

# a=[-9,-8,-7,1,2,3]
# # b=list(filter(lambda x:x>0,a))
# # c=list(filter(lambda x:x<0,a))
# # print(b)
# # print(c)
# x=(reduce(lambda x,y:x+y,a))
# print(x)
# l1=[1,2,3]
# l2=[4,5,6]
# z=list(map(lambda x,y:x+y,l1,l2))
# print(z)

#--------------------------------------- COMPRESSION --------------------------------------------------
# z=[ i*i for i in range(6) ]
# print(z)
# y=[ i*i for i in range(6)  if i%2==0]
# print(y)
