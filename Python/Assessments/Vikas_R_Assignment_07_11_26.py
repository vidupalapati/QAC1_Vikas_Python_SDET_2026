#1. Program to Check whether a number is Positive, Negative, or Zero.

print("Program to Check whether a number is Positive, Negative, or Zero.")

a=int(input("Enter a number: "))
if(a==0):
    print("The entered number is Zero")
elif(a>0):
    print("The entered number is positive")
else:
    print("The entered number is negative")

#2. Program to Check whether a number is Even or Odd.

print("Program to Check whether a number is Even or Odd.")

a=int(input("Enter a number: "))
if a%2==0:
    print(a," is an even number")
else:
    print(a," is an odd number")

#3. program to Find the largest of two numbers.

print("Program to Find the largest of two numbers.")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if(a>b):
    print(a," is larger than ",b)
else:
    print(b," is larger than ",a)

#4. Program to Find the largest of three numbers.

print("Program to Find the largest of three numbers.")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if(a>b and a>c):
    print(a," is largest ")
elif(b>c):
    print(b," is largest ")
else:
    print(c," is largest ")

#5. Program to Check whether a person is eligible to vote.

print("Program to Check whether a person is eligible to vote.")

age=int(input("Enter your age: "))
if(age>18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#6.Program to Check whether a given year is a Leap Year.
# A year is a leap year if it follows these rules:
# Divisible by 4 - leap year
# Divisible by 100 - not a leap year even divisible by 4
# Divisible by 400 - century year is also divisible by 400, it is a leap year

print("Program to Check whether a given year is a Leap Year.")

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

#7. Program to Calculate grade based on marks entered by the user.

print("Program to Calculate grade based on marks entered by the user.")

marks = int(input("Enter your marks: "))
if(marks >= 95 and marks <= 100):
    print("Your grade is A")
elif(marks >= 90 and marks <= 94):
    print("Your grade is A-")
elif(marks >= 87 and marks <= 89):
    print("Your grade is B+")
elif(marks >= 85 and marks <= 86):
    print("Your grade is B")
elif(marks >= 80 and marks <= 84):
    print("Your grade is B-")
elif(marks >= 77 and marks <= 79):
    print("Your grade is C+")
elif(marks >= 75 and marks <= 76):
    print("Your grade is C")
elif(marks >= 70 and marks <= 74):
    print("Your grade is C-")
elif(marks >= 67 and marks <= 69):
    print("Your grade is D+")
elif(marks >= 65 and marks <= 66):
    print("Your grade is D")
elif(marks >= 60 and marks <= 64):
    print("Your grade is D-")
elif(marks < 60 and marks >0):
    print("Your grade is F")
else:
    print("Invalid marks range , Enter marks between 0 to 100")

#8. Program to Check whether a character is a Vowel or Consonant

print("Program to Check whether a character is a Vowel or Consonant")

char = input("Enter a character: ")
if char in ('a', 'A' , 'e','E', 'i', 'I', 'u', 'U', 'o', 'O'):
    print(char," is a Vowel")
else:
    print(char," is a consonant")

#9. Program to Verify a password entered by the user.

print("Program to Verify a password entered by the user.")

password = "Vikas123"
user_password = input("Enter the password: ")
if user_password == password:
    print("Password Verified. Access Granted!")
else:
    print("Incorrect Password. Access Denied!")

#10.Program to Calculate discount based on purchase amount.

print("Program to Calculate discount based on purchase amount.")

bill = float(input("Enter your bill amount: "))

if bill >= 2000:
    discount = bill * 0.25   # 25% discount
elif bill >= 1000:
    discount = bill * 0.15   # 15% discount
elif bill >= 500:
    discount = bill * 0.05   # 5% discount
else:
    discount = 0

final_bill = bill - discount

print("Purchase Amount:", bill)
print("Discount:", discount)
print("Amount to Pay:", final_bill)

#11. Program to Check whether a character is an Alphabet, Digit, or Special Character.

print("Program to Check whether a character is an Alphabet, Digit, or Special Character.")

char = input("Enter a character: ")

if char.isalpha():
    print(char, "is an Alphabet")
elif char.isdigit():
    print(char, "is a Digit")
else:
    print(char, "is a Special Character")

#12. Program to Determine whether a number is a two-digit, three-digit, or more.

print("Program to Determine whether a number is a two-digit, three-digit, or more.")

num = int(input("Enter a number: "))
if(num<0):
    print(num," is a negative number")
elif(num >= 0 and num <10):
    print(num," is a single digit number")
elif(num >= 10 and num <100):
    print(num," is a double digit number")
elif(num >= 100 and num <1000):
    print(num," is a triple digit number")
else:
    print(num," is more than a 3 digit number")

#13. Program to Check whether a character is uppercase or lowercase.

print("Program to Check whether a character is uppercase or lowercase.")

char = input("Enter a character: ")

if char.isupper():
    print(char, "is an Uppercase character")
elif char.islower():
    print(char, "is a Lowercase character")
else:
    print("Entered character is not an alphabet")

#14. Program to Create a simple calculator using conditional statements.

print("Program to Create a simple calculator using conditional statements.")

print("**********************************************************")
print("*****             Enter + for addition               *****")
print("*****             Enter - for substraction           *****")
print("*****             Enter * for multiplication         *****")
print("*****             Enter / for division               *****")
print("**********************************************************")

op = input("Please enter your operation: ")
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
if (op== "+"):
    print ("Addition of ",num1,"and",num2," is ",num1+num2)
elif (op== "-"):
    print ("Substraction of ",num1,"and",num2," is ",num1-num2)
elif (op== "*"):
    print ("Multiplication of ",num1,"and",num2," is ",num1*num2)
elif (op== "/"):
    print ("Division of ",num1,"and",num2," is ",num1/num2)
else :
    print("Please enter a valid operation")

#15. Program to Determine if a day number corresponds to a weekday or weekend.

print("Program to Determine if a day number corresponds to a weekday or weekend.")

# Assume:
#
# 1 = Monday
# 2 = Tuesday
# 3 = Wednesday
# 4 = Thursday
# 5 = Friday
# 6 = Saturday
# 7 = Sunday

day = int(input("Enter a day number (1-7): "))
if(day >=1 and day <=5 ):
    print("Entered day number falls on a weekday")
elif(day == 6 or day == 7):
    print("Entered day number falls on a weekend")
else :
    print("Enter a valid day number between 1 and 7")
