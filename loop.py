#n = int(input("Enter the no: "))\
"""Print Hello Dosto n time"""
# for i in range(n):
#     print("Hello Dosto")

"""Print Natural no to n"""
# for i in range(n+1):
#     print(i)

"""Print Reverse Natural No to n"""
# for i in range(n, 0, -1):
#     print(i)

"""Print Table"""
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")

"""Print the Sum of no. to the n"""
# m = 0
# for i in range(n+1):
#     m = m + i
# print(m)

"""Print factorial to n"""
# m = 1
# for i in range(1,n+1):
#     m = m * i 
# print(m)

"""Find Total Even and Odd no. to n"""
# n = 22
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"Even = {even}, Odd = {odd} ")

"""Print Factors of no. to n"""
# for i in range(1, n+1):
#     if n % i == 0:
#         print(f"Factors of {n} = {i}")

"""Find the perfect no."""
# m = 0
# for i in range(1, n):
#     if n % i == 0:    
#         m = m + i
# if m == n:
#     print(f"{n} is a perfect no.")
# else:  
#     print(f"{n} is a ordinary no.")  
        
"""Finding the no. is prime or not"""
# factor = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         factor = factor + 1
# if factor == 2:
#     print("The no. is a Prime no")
#     print(f"Total no of Factors {factor}")
# elif factor <= 1:
#     print("The no. is neither Prime nor Composite")
#     print(f"Total no of Factors {factor}")
# else:
#     print("The no is a Composite no.")    
#     print(f"Total no of Factors {factor}")

"""Reverse a String"""
# a = "Hello"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# print(b)    

"""String is palindrome or not"""
# a = "naman"
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# if a == b:
#     print("The String is Palindrome")
# else:
#     print("The String is not Palindrome")    

"""Counting all the digit character and special character"""
# a = "723fnkjh*)&^Biuy87OBU)!@"
# digit = 0
# char = 0
# SpecChar = 0

# for i in a:

#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         SpecChar += 1

# print(f"Digit = {digit}, Character = {char}, Special Character = {SpecChar}")

"""Seperate any no. non-sequential"""
# a = 890
# while a > 0:
#     print(a % 10)
#     a = a // 10

"""Comibe the no non-sequential"""
# a = 876
# b = 0
# while a > 0:
#     b = b * 10 + a % 10
#     a = a // 10
# print(b)

"""Palindrome no."""
# a = 1221
# b = 0
# c = a
# while a > 0:
#     b = b * 10 + a % 10
#     a = a // 10
# if b == c:
#     print("The no. is Palindrome")
# else:
#     print("The no. is not Palindrome")

"""Random no. Guessing Game"""
import random

num = random.randint(1,10)
tries = 0

while True:
    a = int(input("Enter the no: "))
    if a == num:
        tries += 1
        print("Congratulation you Gussed the number")
        break

    elif tries == 5:
        break

    elif a > num:
        tries += 1
        print("The number is a little smaller")
    else:
        tries += 1
        print("The number is a little Bigger") 
        
if a == num:
    print(f"You take total tries: {tries}")
else:
    print("You Lost")
    print(f"The no. was: {num} Total tries: {tries}")
        
        
