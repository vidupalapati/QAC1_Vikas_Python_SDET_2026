"""
Dictionary :

Whenever we want to represent a group of values as key:value pairs , we go with the dictionary .

	® In other programming languages we call it as Map.
	® Duplicate keys are not allowed but values can be duplicate.
	® Heterogeneous values are allowed for both key and values.
	® Insertion order is not preserved .
	® Dictionaries are mutable.
	® Dictionaries are dynamic in nature .
	® Indexing and slicing concept is not applicable.

"""
#WAP to display student_name , marks in dictionary format)

# d={}
# n=int(input("Enter the number of students : "))
# i=1
# while i<=n:
#     name= input("Enter Name : ")
#     marks= int(input("Enter Marks : "))
#     d[name]=marks
#     i=i+1
#
# print("Name of the student ","/t/t/t/t/t/t","% of marks")
# for x in d:
#     print(x,"/t/t/t/t/t/t",d[x]/n)

#WAP to take a dictionary from keyboard and print sum of values
# d=eval(input("Enter the dictionary : "))
# s=sum(d.values())
# print(s)

#WAP to count the number of times a char is repeated in a given string

# name = "Vikas Vidupalapati"
# d={}
# for i in name:
#     d[i]=d.get(i,0)+1
# for k,v in d.items():
#     print(k,"repeated ",v," times ")

#WAP to find number of vowels present in given word
d={}
vowels={'a','e','i','o','u'}
name="Vikas Vidupalapati"
for i in name:
    if i in vowels:
        d[i]=d.get(i,0)+1
for k,v in d.items():
    print(k,"repeated ",v," times ")
