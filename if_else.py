# a = int(input("Enter the Choosen no.: "))
# b = int(input("Enter the Choosen no.: "))

# if a > b:
#     print(f"{a} is Greather than {b}")
# else:
#     print(f"{b} is Greather than {a}")    

# gender = input("Please Enter your Gender (Male/female): ")

# if gender == "Male" or gender == "male":
#     print("Good Morning Sir")
# elif gender == "Female" or gender == "female":
#     print("Good Morning Ma'am") 
# else:
#     print("Unidentified Gender")

# a = int(input("Please Enter the choosen no: "))
# if a % 2 == 0:
#     print("The no. is Even")
# else:
#     print("The no. is Odd")

# name = input("Please enter your name: ")
# age  = int(input("Please enter your age: "))

# if age >= 18:
#     print(f"Congrats, {name} you are a valid voter. You can vote")
# elif 0 < age < 18:
#     print(f"{name}, Sorry you can not vote")
# else:
#     print("Please enter a Valid Age")    

# year = int(input("Enter the year: "))

# if year % 100 and year % 400 == 0:
#     print("The year is Leap year")
# elif year == 100 != 0 and year % 4 == 0:
#     print("The year is Leap year")
# else:
#     print("The year is Ordinary year")   
# 

temp = int(input("Enter the temperature: "))

if temp < 0:
    print("Freezing cold❄️")
elif 0 <= temp < 10:
    print("Very Cold🧊") 
elif 10 <= temp < 20:
    print("Cold🤧")
elif 20 <= temp < 30:
    print("Pleasant😎")
elif 30 <= temp < 40:
    print("Hot♨️")
else:
    print("Very Hot🌋")       