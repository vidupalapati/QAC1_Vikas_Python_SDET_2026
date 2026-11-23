"""
Operators

Operator is a symbol that performs certain operations.

Python provides the following set of operators
1. Arithmetic Operators
2. Relational Operators or Comparison Operators
3. Logical operators  4. Bitwise operators
5. Assignment operators
6. Special operators

1.  Arithmetic Operators:
+ ==>Addition
- ==>Subtraction
* ==>Multiplication
/ ==>Division operator (O/P will be in floating values)
% ==>Modulo
// ==>Floor Division operator (O/P in integer format until any one of the Operand is float)
** ==>Exponent operator or power operator
"""

a=300
b=100

print(a+b) #Addition
print(a-b)
print(a*b) # Multiplication
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# we can use + and * for string operations

s1="hello"
s2="world"

print(s1+s2) #Concatenation - Both arguments should be strings
print(s1*2) #Repeatation - One argument should always be Int type

"""
2. Relational Operators or Comparison Operators

	• Greater than (>)
	• Greater than or equal to (>=)
	• Less than (<)
	• Less than or equal to (<=)
"""
a=100
b=200
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print ("************************************************")

#Equality Operators - == and !=

print(a==b)
print(a!=b)

print ("************************************************")

#we can also use for strings - compares ASCII values

s1="hello"
s2="world"

print(s1>s2)
print(s1<s2)
print(s1>=s2)
print(s1<=s2)

"""
3. Logical Operators:  and, or ,not  


"""