#-------------------------------------------- QUE NO:295----------------------------------------------
# a="RAJ"
# b=a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("NOT PALINDROME")


#-------------------------------------------- QUE NO:298----------------------------------------------
# def upper():
#     x="RAJraval"
#     u=0
#     l=0
#     for i in x:
#         if i.isupper():
#             u+=1
#         elif i.islower():
#             l+=1
#     print(f"upper:{u}, lower:{l}")
# upper()


# def pb():
#     a=int(input(" ENTER NUMBER:"))
#     b=int(input(" ENTER SHIFT:"))
#     c=str(a)
#     if b>len(c):
#         print(c[::-1])
#     else:
#         print(c[b:]+c[0:b])
# pb()

# key=3
# a="abc"
# encrypt=""
# for i in a:
#     encrypt+=chr(ord(i)+key)
# print(encrypt)
#if entered xyz the o/p should be abc , so if key goes out of range the number should be reversed

#-------------------------------------------- QUE NO:300----------------------------------------------

# a=input("ENTER A STRING:")
# b=int(input("ENTER THE PLACE NUMBER FROM WHICH YOU WANT TO REMOVE THE CHARACTER:"))
# print(a[:b]+a[b+1:])

#-------------------------------------------- QUE NO:301----------------------------------------------

# a=input("ENTER STRING:")
# b=a.split(" ")
# for i in b:
#     print(i[0]+i[len(i)//2]+i[-1])

#-------------------------------------------- QUE NO:302 ----------------------------------------------

# a=input("ENETR A STRING:")
# b=input("ENTER A SUBSTRING TO CHECK :")
# print(a.find(b))

#-------------------------------------------- QUE NO:303 ----------------------------------------------

# a=input("ENTER A STRING:")
# d=0
# c=0
# for i in a:
#     if i.isdigit():
#         d+=int(i)
#         c+=1
# if d==0:
#     print(" NO DIGITS ARE THERE IN STRING")
# print(f"THE SUM OF DIGIT IS :{d} , and the average is {d/c}")

#-------------------------------------------- QUE NO:304 ----------------------------------------------

# a=input("ENTER A STRING:")
# print(a[::-1])

#-------------------------------------------- QUE NO:305 ----------------------------------------------

# a=input("ENTER A STRING:")
# b=a.split(" ")
# for i in b:
#     if len(i)%2==0:
#         print(i)

#-------------------------------------------- QUE NO:306 ----------------------------------------------

# a=input("ENTER A STRING")
# print(a[:(len(a)//2)+1].upper())

#-------------------------------------------- QUE NO:308 ----------------------------------------------

# a=input("ENTER A STRING:")
# print(a[(len(a)//2)-1:(len(a)//2)+2:])

#-------------------------------------------- QUE NO:309 ----------------------------------------------

# a=input("ENTER A STRING:")
# b=input("ENTER A SECOND SSTRING TO MATCH WITH THE FIRST ONE :")
# balanced=True
# for i in a:
#     if i not in b:
#         balanced=False
#         break
# if balanced:
#     print(" THE STRINGS ARE BALANCED")
# else:
#     print(" THE STRINGS ARE NOT BALANCED ")

#-------------------------------------------- QUE NO:316----------------------------------------------

# a=input("ENTER PASSWORD:")
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

#-------------------------------------------- QUE NO:317 ----------------------------------------------

# a=input("ENTER A STRING:")
# result=""
# for i in a:
#     if i.isupper():
#         result+=i.lower()
#     elif i.islower():
#         result+=i.upper()
#     else:
#         result+=i
# print(f"THE NEW STRING WITH SWAPPED CASE IS :{result}")

#-------------------------------------------- QUE NO:318 ----------------------------------------------


text = input("Enter the input text: ")
shift = int(input("Enter the shift value: "))

cipher = ""

for char in text:
  if char.isupper():
    cipher += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
  elif char.islower():
    cipher += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
  else:
    cipher += char

print(f"Cipher: {cipher}")

# b=input("ENTER A STRING:")
# keys=int(input("ENTER THE NUMBER OF KEYS:"))
# a="ABCDEFHIJKLMNOPQRSTUVWXYZ"
# b=b.upper()
# ans=""
# for i in b:
#     if i in a:
#         p=((a.find(i)+keys))%26
#         ans=ans+a[p]
#     else:
#         ans=ans+i
# print(ans)


#-------------------------------------------- QUE NO:400 ----------------------------------------------

# def special_count(a):
#     special_elem=0
#     n=len(a)
    

#     for i in range(n):
#         temp_list= a[:i]+a[i+1:]

#         even=0
#         odd=0

#         for j in range (len(temp_list)):
#             if j%2==0:
#                 even+=temp_list[j]
#             else:
#                 odd+=temp_list[j]
#         if even==odd:
#             special_elem+=1

#     return special_elem

# print(special_count([5,5,2,5,8]))

#-------------------------------------------- QUE NO:401 ----------------------------------------------
# def syracuse(a):
#     x=a
#     print(f"THE STARTING NUMBER OF THE SEQUENCE IS : {x} ")
#     l=[]
#     while x!=1:
#         if x%2==0:
#             x=x//2
#             # print(x)
#             l.append(x)
#         else:
#             x=3*x+1
#             # print(x)
#             l.append(x)
#     print(l)

# a=int(input(" ENETER A NUMBER :"))
# syracuse(a)

#-------------------------------------------- QUE NO:434 ----------------------------------------------

# def missing_smallest(a):
#     smallest = 1
#     while True:
#         found = False
#         for i in a:
#             if i == smallest:
#                 found = True
#                 break
#         if not found:
#             return f"THE SMALLEST POSITIVE MISSING NUMBER IS {smallest}"
#         smallest += 1

# print(missing_smallest([10, 0, 3, -4, 2, 1]))


#-------------------------------------------- QUE NO:440 ----------------------------------------------

# l=[1,2,-14,5,-12,-24,3,4]
# positive=sum(filter(lambda x:x>0,l))
# negative=sum(filter(lambda x:x<0,l))
# print(f"THE SUM OF ALL POSITIVE NUMBERS IS :{positive} THE SUM OF ALL THE NEGATIVE NUMBERS IS :{negative}")

#-------------------------------------------- QUE NO:443 ----------------------------------------------

# def group(a):
#     d={}
#     for i in a:
#         if i not in d:
#             d[i] = [i]
#         else:
#             d[i].append(i)
#     sort_tup=sorted(d.items(),key=lambda x:len(x[1]),reverse=True)
#     return dict(sort_tup)

# print(group([4, 6, 6, 4, 2, 2, 4, 8, 5, 8]))

#-------------------------------------------- QUE NO:444 ----------------------------------------------

# def rotate_matrix_90_clockwise(A):
#     N = len(A)
    
#     # Step 1: Transpose the matrix in-place
#     for i in range(N):
#         for j in range(i + 1, N):
#             A[i][j], A[j][i] = A[j][i], A[i][j]
            
#     # Step 2: Reverse each row in-place
#     for i in range(N):
#         left = 0
#         right = N - 1
#         while left < right:
#             A[i][left], A[i][right] = A[i][right], A[i][left]
#             left += 1
#             right -= 1

# # 1. Get N from the user
# N = int(input("Enter the value of N (1 to 20): "))

# # 2. Get the N x N matrix from the user row by row
# A = []
# print(f"Enter the matrix elements row by row ({N} values separated by spaces for each row):")
# for i in range(N):
#     row = [int(x) for x in input(f"Row {i+1}: ").split()]
#     A.append(row)

# # 3. Rotate the matrix in-place
# rotate_matrix_90_clockwise(A)

# # 4. Print the rotated matrix
# print("\nRotated Matrix (90 degrees clockwise):")
# for row in A:
#     print(row)


#-------------------------------------------- QUE NO:445 ----------------------------------------------

# a = ["lessonplan", "lesson", "lees", "length"]
# a.sort()
# ans = ""
# print("Sorted list:", a)

# for i in range(min(len(a[0]), len(a[-1]))):
#     if a[0][i] == a[-1][i]:
#         ans = ans + a[0][i]
#     else:
#         break

# if ans:
#     print(f"The longest Common Prefix is: {ans}")
# else:
#     print("-1")

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum)
