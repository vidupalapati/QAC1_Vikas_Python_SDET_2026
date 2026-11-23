"""
In python 2.0
Raw Input()
input()

In python 3.0
input()
"""
# name = input("Enter your name: ")
# print(name,type(name))

# all the inputs are treated as string by default
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# num3 = input("Enter another number: ")
# num4 = num1 + num2 + num3
# print(num4)

#to convert the input into other types we have to do typecasting

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter another number: "))
# sum = num1 + num2 + num3
# print(sum)

#eval() - eveluates the given source in the context of globals and locals
# exp = eval("20+30-40*60/4")
# print(exp)
# print(type(exp))

# String format method
name = 'Vikas'
age = 30
Salary = 60000
print(name,age,Salary)
print("My name is {},my age is {},my salary is {}".format(name,age,Salary))
print("My name is {},my age is {},my salary is {}".format(Salary,name,age))
#The above print statement prints inappropriately

print("My name is {y},my age is {z},my salary is {x}".format(x=Salary,y=name,z=age))
