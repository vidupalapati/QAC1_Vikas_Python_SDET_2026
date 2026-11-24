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
"""

#Reversing a string
name ="Vikas"
print(name[::-1])

#palindrome
s=input("Enter a string : ")
if s==s[::-1]:
    print(s," is a palindrome")
else:
    print(s, " is not a palindrome")





