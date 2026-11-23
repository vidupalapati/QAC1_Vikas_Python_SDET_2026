# Working with random module

#random() function ==> 0<x<1 floating point values b/w 0 and 1

from random import *

# for i in range(10):
#     print(random())

#randint() function : random integer b/w 2 given numbers

# for i in range(10):
#     print(randint(1,100))

#uniform() function - random floating point values b/w 2 given numbers

# for i in range(10):
#     print(uniform(90,100))

#randrange(start,stop,step)

# for i in range(10):
#     print(randrange(10))
#
# print("++++++++++++++++++++++++++++++++++++++++")
#
# for i in range(10):
#     print(randrange(10,50))
#
# print("++++++++++++++++++++++++++++++++++++++++")
#
# for i in range(10):
#     print(randrange(0,100,9))

#choice() function - may print duplicate values if the interval is small

list=[100,200,300,400,500,600,700,800,900]
for i in range(10):
    print (choice(list))