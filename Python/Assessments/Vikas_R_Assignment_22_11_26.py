"""
#Pattern-1
for i in range(1,11):
    for j in range(1,11):
        print(j,end=" ")
    print()

#Pattern-2
for i in range(1,11):
    for j in range(1,11):
        print(i,end=" ")
    print()

#Pattern-3
a=65
for i in range(1,11):
    for j in range(1,11):
        print(chr(a),end=" ")
    print()
    a=a+1

#Pattern-4
for i in range(1,11):
    for j in range(65,75):
        print(chr(j),end=" ")
    print()

#Pattern-5
for i in range(1,11):
    for j in range(10,0,-1):
        print(j,end=" ")
    print()

#Pattern-6
for i in range(10,0,-1):
    for j in range(1,11):
        print(i,end=" ")
    print()

#Pattern-7
for i in range(74,64,-1):
    for j in range(1,11):
        print(chr(i),end=" ")
    print()

#Pattern-8
for i in range(1,11):
    for j in range(74,64,-1):
        print(chr(j),end=" ")
    print()

#Reversing a string
name ="Vikas"
print(name[::-1])

#palindrome
s=input("Enter a string : ")
if s==s[::-1]:
    print(s," is a palindrome")
else:
    print(s, " is not a palindrome")


#fibonacci series

def fib (n):
    a, b = 0, 1
    print(a,b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a = b
        b = c

num=int(input("Enter a number of terms : "))
fib(num)

#Armstrong number

num = int(input("Enter a number: "))

temp = num
sum = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

#Prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")

#Factorial of a number
num = int(input("Enter a number: "))
Fact=1

if num > 1:
    for i in range(1,num+1):
        Fact*= i
    print("Factorial of ",num," is",Fact)
else :
    print("Enetr a number greater than Zero")

#Count the Occurrence of Characters in a String.
s = input("Enter a string: ")
visited = ""
for i in s:
    if i not in visited:
        count = 0
        for j in s:
            if i == j:
                count += 1
        print(i, "is present", count, "times")
        visited += i
"""
#Remove Duplicates from a List.
x=[] #empty list
num = int(input("Enter the number of elements in list: "))
#reading list elements from keyboard and storing them in list
for i in range(num):
    s=input("Enter the list element: ")
    x.append(s)
#removing duplicates from list
visited = []
for i in x:
    if i not in visited:
        count = 0
        for j in x:
            if i == j:
                count += 1
        visited.append(i)
    if count > 1:
        x.remove(i)
print("The list after removing duplicates is : ",x)


