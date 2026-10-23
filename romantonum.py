# def romantonum(x):
#     num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
#     roman=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
#     roman_num=""
#     i=12
#     while x!=0:
#         if num[i]<=x:
#             roman_num+=roman[i]
#             x=x-num[i]
#         else:
#             i-=1
#     return roman_num
# x=int(input("ENTER A NUMBER:"))
# print(romantonum(x))

# def roman(x):
#     num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#     roman=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
#     rnum=""

#     for i in range(len(num)):
#         while x>=num[i]:
#             rnum+=roman[i]
#             x-=num[i]
#     print(rnum)
# x=int(input("ENTER A NUMBER:"))
# roman(x)


def numtoroman(a):
    values={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    n=0

    for i in range(len(a)):
        if i+1<len(a) and values[a[i]]<values[a[i+1]]:
            n=n-values[a[i]]
        else:
            n=n+values[a[i]]
    return n
b=input("ENETR A ROMAN NUMBER:") 
a=b.upper()
print(numtoroman(a))   