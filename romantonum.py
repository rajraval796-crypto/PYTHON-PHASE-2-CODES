def romantonum(x):
    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    roman_num=""
    i=12
    while x!=0:
        if num[i]<=x:
            roman_num+=roman[i]
            x=x-num[i]
        else:
            i-=1
    return roman_num
x=int(input("ENTER A NUMBER:"))
print(romantonum(x))
