#--------------------------------------- code 1 --------------------------------------------------

# d={"a":10,"b":20,"c":30,"d":40}
# for i,j in d.items():
#     if j==40:
#         print(i)

#--------------------------------------- code 2 --------------------------------------------------

# d={"a":10,"b":20,"c":30,"d":40,"e":90}
# li=d.values()
# maxi=max(li)
# mini=min(li)
# for i,j in d.items():
#     if j==maxi:
#         print(f" THE MAXIMUM IS {i}")
#     if j==mini:
#         print(f" THE MINIMUM IS {i}")


# --------------------------------------- code 3 --------------------------------------------------

# get fun in dict
# syntax: d.get("key", here enter something in case the key is not found )
# d={"a":110,"b":220,"c":-30,"d":-40,"e":900}
# print(d.get("a",0))
# z=sorted(d.items(),key=lambda x:x[1],reverse=True)
# z=sorted(d.items(),key=lambda x:x[0],reverse=True)
# print(z)

#--------------------------------------- code 4 --------------------------------------------------

# d={"a":100,"b":80,"c":30,"d":0,"e":101}
# z=sorted(d.items(),key=lambda x:x[1],reverse=True)
# # print(z[0][0],z[1][0],z[2][0])
# for i in z[:3]:
#     print(i[0])

#--------------------------------------- code 5 --------------------------------------------------
# d={}
# s="abchdgfssaas ++"
# for i in s:
#     # d[i]=s.count(i)
#     d[i]=d.get(i,0)+1
# print(d)

#--------------------------------------- code 6 --------------------------------------------------
# x="dhruv dhruv dhoni dhoni rohit"
# z=x.split(" ")
# d={}
# for i in z:
#     # d[i]=s.count(i)
#     d[i]=d.get(i,0)+1
# print(d)

# #--------------------------------------- code 7 --------------------------------------------------
                    # ------------------ 9 MARKS CODE ----------------------
# a=int(input("ENTER A NUMBER:"))

# d = {
#     0:"",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
#     10: "ten",
#     11: "eleven",
#     12: "twelve",
#     13: "thirteen",
#     14: "fourteen",
#     15: "fifteen",
#     16: "sixteen",
#     17: "seventeen",
#     18: "eighteen",
#     19: "nineteen",
#     20: "twenty",
#     30: "thirty",
#     40: "forty",
#     50: "fifty",
#     60: "sixty",
#     70: "seventy",
#     80: "eighty",
#     90: "ninety",
#     100: "hundred",
# }

# def ans(a):
#     if a<=20:
#         return d[a]
#     elif a<100:
#         f=(a//10)*10
#         l=a%10
#         return d[f]+""+d[l]
#     elif a<1000:
#         f1=(a//100)
#         l1=a%100
#         return d[f1]+" "+"HUNDRED"+" "+ans(l1)
# c=ans(a)
# print(c)

#--------------------------------------- code 8 --------------------------------------------------


x = "dhruv dhruv dhoni dhoni rohit"
z=x.split(" ")
d = {}
for i in z:
    if i not in d:
        d[i] = i
    else:
        d[i] += " " + i

print(d)