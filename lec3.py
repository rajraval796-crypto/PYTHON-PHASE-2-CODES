#--------------------------------------- code 1 --------------------------------------------------
# l1=[] 
# l2=list(range(1,20))
# print(l2)
# l1.extend(l2)
# print(l1)
# l2.append(20)
# print(l2)
# l2.pop()
# del l2[15]
# print(l2)
# l2.insert(5,"RAJ")
# l3=[88,00,-456,90,60,495,999]
# print(max(l3))
# print(sorted(l3))
# l1.clear()
# print(l1)

#--------------------------------------- code 2 --------------------------------------------------
# l3=[88,00,-456,90,60,495,999]
# even=[]
# odd=[]
# for i in l3:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(max(even))
# print(max(odd))

#--------------------------------------- pb code 1 --------------------------------------------------
# l=[1,2,3,4,5,6,7,8]
# even=[]
# for i in l:
#     if i%2==0:
#         print(i)
#--------------------------------------- pb code 2 --------------------------------------------------
# l=[1,2,3,4,5,6,7,8]
# even=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
# print(max(even))

#--------------------------------------- pb code 3 --------------------------------------------------
# a=eval(input(" ENETR A LIST :"))
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         even.append(i)
# print(f"THE LARGEST ODD IS : {max(odd)}")
# print(f"THE LARGEST EVEN IS : {max(even)}")

#--------------------------------------- pb code 4 --------------------------------------------------
# l1=list(range(1,51))
# even=[]
# odd=[]
# for i in l1:
#     if i%2==0:
#         even.append(i)
#     else:
#         even.append(i)
# even.sort()
# odd.sort()
# print(f"THE MAXIMUN IS:{even[-1]}")
# print(f"THE  SECOND MAXIMUN IS:{even[-2]}")
# print(f"THE   MAXIMUN IS:{odd[-2]}")
# print(f"THE  SECOND MAXIMUN IS:{odd[-2]}")

#--------------------------------------- pb code 5 --------------------------------------------------
# a=[2,4,-6,-9,11,-12,14,-5,17]
# pos=[]
# neg=[]
# for i in a:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"THE SUM OF POSITIVE NUMERS IS {sum(pos)}")
# print(f"THE SUM OF NEGATIVE NUMERS IS {sum(neg)}")

#--------------------------------------- pb code 6 --------------------------------------------------

# a=["abc","xyz","aba","2112","123451","12345"]
# c=0
# for i in a:
#     if len(i)>=3:
#         if i[0]==i[-1]:
#             c+=1
# print(c)

#--------------------------------------- pb code 7 --------------------------------------------------

# a=[2,4,6,8,10]
# for i in range(len(a)):
#     if i %2 !=0:
        
#         a.insert(i,max(a))
#         del(max(a))
# print(a)
