#--------------------------------------- code 1 --------------------------------------------------
# d="dhruv dhoni dh nb kj po"
# k=d.split(" ")
# d={}

# for i in k :
#     d[i]=len(i)
# print(d)


#--------------------------------------- code 2 --------------------------------------------------

# l=[20,30,40,1,5,9,8]
# l2=[]
# l3=[]
# d={
#     1:"one",
#     2:"two",
#     3:"three",
#     4:"four",
#     5:"five",
#     6:"six",
#     7:"seven",
#     8:"eight",
#     9:"nine",
# }

# for i in l:
#     if i>0 and i<10:
#         l2.append(i)
# l2.sort(reverse=True)
# print(l2)

# for i in l2:
#     l3.append(d[i])
# print(l3)

#--------------------------------------- MAKETRANS --------------------------------------------------
s="RAJ RAVAL 651652"
t=str.maketrans("RAJ","HIJ","651652")
print(t)
z=s.translate(t)
print(z)
