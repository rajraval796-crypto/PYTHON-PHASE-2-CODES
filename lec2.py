#----------------------------------------- code 1 ------------------------------------------------
# a="RAj@67"
# u=0
# l=0
# d=0
# s=0
# spe=0

# if len(a)<8:
#     print(" INVALID PASSWORD ")
# else:
#     for i in a:
#         if i.isupper():
#             u+=1
#         elif i.islower():
#             l+=1
#         elif i.isdigit():
#             d+=1
#         elif i.isspace():
#             s+=1
#         else:
#             spe+=1
#     if u>0 and l>0 and d>0 and spe>0 and s==0:
#         print(" VALID PASSWORD")
#     else:
#         print("INVALID PASSOWRD")

#----------------------------------------- code 2 ------------------------------------------------


# a="RAJ RAVAL LIVES ON EARTH"
# b=a.split(" ")
# print(b)
# for i in b:
#     print(i,end=" ")
# print()
# for i in b:
#     if len(i)%2==0:
#         print(i)

#----------------------------------------- code 3------------------------------------------------


# a="dhruv python ai"
# b=a.split(" ")
# for i in b:
#     print(i[::-1],end=" ")


#----------------------------------------- code 4 ------------------------------------------------


# a="dhruv python coding website ai ml data powerbi django"
# b=a.split(" ")
# for i in b:
#     if len(i)>5:
#         print(i)


#----------------------------------------- code 5 ------------------------------------------------

# a="dhruv dhoni rohit"
# b=a.split(" ")
# for i in b:
#     print(i[0].upper()+i[1:-1]+ i[-1].upper())

#----------------------------------------- code 6 ------------------------------------------------

# a="dhruv dhoni rohit"
# b=a.split(" ")
# for i in b:
#     print(i[0].upper()+i[-2:0:-1]+ i[-1].upper())

#----------------------------------------- code 7 ------------------------------------------------

# a="dhruv python coding website ai ml data powerbi django "
# b=a.split(" ")
# for i in b:
#     if len(i)%2==0:
#         print(i.upper())
#     else:
#         print(i.lower())

#----------------------------------------- code 8 ------------------------------------------------
x="RAJR"
print(x.find("JR"))
print(x.find("A"))
print(x.find("A"))
print(x.index("A"))
# print(x.index("H"))
print(x.rindex("R"))
print(x.rfind("R"))