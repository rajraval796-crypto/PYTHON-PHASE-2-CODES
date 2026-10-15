# --------------------------------code 1-----------------------------------------------
#  x="abcd_efg_hij"
# print(x[-1]) 
# print(x[3:9:2]) 
# print(x[::])
# print(x[9::1])
# print(x[15::1])  
# print(x[::5])
# print(x[1::5])
# print(x[::20])
# print(x[3:4:10])
# print(x[2]) 
# print(x[-7:-4:])
# print(x[-7:-1:-1])
# print(x[-13::]) 
# print(x[::-1])

# ------------------------------------------code 2---------------------------------------------
# y="I LOVE INDIA "
# print(y[0]+y[5:1:-1]+y[7::])

#----------------------------------------- code 3 ----------------------------------------------------

# x="RAJ"
# y="raval"
# z=" "
# d="Raj raVAL"
# a="1234"
# b="abcd1213"
# c="abcd1213_"
# print(x.lower())
# print(y.upper())
# print(d.swapcase())
# print(d.title())
# print(d.count("a"))
# print(d.replace("a","A"))
# print(x.isupper())
# print(y.islower())
# print(a.isdigit())
# print(a.isalpha())#checks for A-Z and a-z in string 
# print(b.isalnum())
# print(z.isspace())
# print(c.isalnum())


#----------------------------------------- code 4 -------------------------------------

# x=" Dhruv DHoni iPL"
# # hDruv INOhd LPI
# print(x[2]+x[1]+x[3:6]+x[6]+(x[11:6:-1]).swapcase()+x[6]+(x[-1:-3:-1]).upper()+(x[-3]).upper())


#----------------------------------------- code 5 ------------------------------------------
# x="Dhruv 77dhONI"
# u=0
# l=0
# d=0
# s=0
# for i in x:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     elif i.isspace():
#         s+=1
# print(f"upper:{u}, lower:{l} , digit:{d} , space:{s}")

#------------------------------------------- code 6 -----------------------------------------------

# x="dhRUV@1127"
# u=0
# l=0
# d=0
# s=0
# spe=0
# for i in x:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     elif i.isspace():
#         s+=1
#     else:
#         spe+=1
# print(f"upper:{u}, lower:{l} , digit:{d} , space:{s} , special:{spe}")

#------------------------------------------- code 7 -----------------------------------------------

x="RAJ   RAVAL"
y=x.title()
for i in y:
    if i.isupper():
        print(i,end="")






