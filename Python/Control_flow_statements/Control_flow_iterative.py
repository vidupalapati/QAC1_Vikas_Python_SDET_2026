# #For loop - if we want to execute some action on every element
# # present in some sequence (String,Collection,etc…)
#
# """
# SYNTAX :
#
# for <var_name> in sequence:
#     body
# """
# list =[10,20,30,40,50]
#
# for i in list:
#     print(i)
#
# #WAP using for loop to display the +ve and -ve index of the given string
# str = "Vikas Vidupalapati"
# len_str = len(str)
# count=0
# for i in str:
#     print ("The +ve index of character ",i,"is",count,"The -ve index is",count-len_str)
#     count+=1
#
# #WAP to print given string 10 times
# for i in range(10):
#     print("Vikas Vidupalapati")
#
# #WAP to print odd numbers from 1 to 20
# for i in range(0,20):
#     if(i%2!=0):
#         print(i,"is Odd number")

#While Loop - If we want to execute group of iterative statements until
#some condition fails then we should go for while loop
"""
SYNTAX :
while condition:
    body
"""
# name=""
# while name!="Hello":
#     name = input("Enter your name")
# print("Thank you for your time")

# i=0
# while True:
#     i=i+1
#     print(i)
