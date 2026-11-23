s="Vikas Vidupalapati"

# print(len(s))

#WAP to access each char of a string both forward and backward direction
#using for loop

# #forward direction
# for i in s:
#     print(i,end='')
# print()
#
# #backward direction
# for i in s[::-1]:
#     print(i,end='')

#WAP to access each char of a string both forward and backward direction
#using while loop

#forward
# n=len(s)
# i=0
# while i<n:
#     print(s[i],end=" ")
#     i=i+1

#backward
# i=-1
# while i>=-n:
#     print(s[i],end=" ")
#     i=i-1

#String Comparison
# s1=input("Enter the first string : ")
# s2=input("Enter the second string : ")
#
# if s1==s2:
#     print("Both strings are equal")
# elif s1<s2:
#     print("The first string is smaller")
# else:
#     print("The first string is larger")

#WAP to remove space from a given string
# s="           Vikas           "
# print(s.strip()) #removes spaces from both the sides
# print(s.lstrip()) #removes spaces from left side of the string
# print(s.rstrip()) #removes spaces from right side of the string

#find () - returns the index of first occurance of given substring
# s="Learning playwright with python"
# print(s.find("play"))
# print(s.find("play",12,20))
#returns -1 as the substring play is not present from index 12 to 20

#replace() - replaces one substring with another substring

# s="Learning Python"
# print(s,id(s))
# s1=s.replace("Python","Playwright")
# print(s1,id(s1))

#split() - returns the list of substrings with seperator string
# s="learning python with playwright"
# l=s.split(" ")
# print(l,type(l))

#join() - The join() method in Python is used to combine elements of
#an iterable (like a list, tuple, or string characters) into a single string.

# words = ["Python", "is", "awesome"]
# result = " ".join(words)
# print(result)

#reversing a string

#using negative index

# print(s[::-1])

#using join() method

# reversed_string = ''.join(reversed(s))
# print(reversed_string)

#using while loop

# i=len(s)-1
# target=''
# while i>=0:
#     target+=s[i]
#     i-=1
# print(target)

# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

# print("BG123".isalnum())
# print("BG123".isalpha())
# print("BG".isalpha())
# print(" ".isspace())