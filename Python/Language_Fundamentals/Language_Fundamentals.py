print ('hello')

x='Vikas'
y='Vikas'

print (x,id(x))
print (y,id(y))

x=100
x1='200'

# List Datatype

x=[100 ,200 ,34.56,46.98,'Vikas','Lavanya',10+6j,True,False,200]
print (x)
print (type(x))
x.append(222)
print (x)
x.remove(100)
print(x)
print (x.count(200))
x.insert (1,250)
print (x)
x.reverse()
print (x)
print (x.index(250))

#Tuple
# works exactly as list except it is immutable
# enclosed by () parenthesis ==> Optional
#Objects are seperated by comma (,)

t= (10,20,30,True,False,"Vikas")
print (t)
print (type(t))
x=t[3]
print (x)

#Range Datatype :
#Used to represent sequence of numbers
#case-1 - range (10)
for i in range(10) : print (i,end=' ')
print()
#case-2 - range (11,21) (start,end)
for i in range(11,21) : print (i,end=' ')
print()
#case-3 - range (0,100,9) (start,end ,step)
for i in range (0,100,9):print (i,end=' ')
print()
#set Datatype
s= {100,200,300,"BG","Vikas","Lavanya",100,200,300,10.2,11.8,"BG",100,200,300}
print (s)
s.add(True)
print (s)
s.remove("Vikas")
print (s)
print (type(s))

S2={}
print (type(S2))

#creating an empty set
s1 = set()
print (type(s1))

#FrozenSet Datatype : Immutable
fs=frozenset(s)
print (fs)
print (type(fs))

#Dictionary Datatype : Mutable
# also called as Map in JAVA
#Stored as Key value pairs {Key : Value}
# Roll number ==> Your name
# college code ==> Department
# Car ==> Model name

d={}
print (d)
print (type(d))

d['a'] = 100
d['b'] = 200
d['c'] = 300
d['name'] = 'Vikas'

print (d)

# We can update the values for a key

d['a']  = 2000
print (d)

#None Datatype
#In java we call it as Null

x=100
print (type(x))
print (x)

x=None
print (type(x))
print (x)

def hello():
    None
hello ()

#Escape Chars
print("hello 'Everyone'!!! , Good Morning")
# print("hello "Everyone"!!! , Good Morning")
print("hello 'Everyone\\'!!! , Good Morning")
print("hello 'Everyone\\'!!!\n , Good Morning") #New line
print("hello 'Everyone\\'!!!\t,Good Morning") #tab space




