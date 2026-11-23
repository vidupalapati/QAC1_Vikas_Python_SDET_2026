"""
1. break
2. continue
3. pass
"""

#break - whenever we wnat to break the loop based on our condition

# i=0
# while True:
#     i=i+1
#     print(i)
#     if(i==250):
#         break

#continue - when we want to skip current iteration
#and continue with rest of the iteration

# cart=[100,200,300,400,500,600]
# for i in cart:
#     if i>400:
#         print("We cannot order this product",i)
#         continue

#WAP to print odd number from 1 to 20
# for i in range(20):
#     if i % 2 == 0:
#         continue
#     print(i,end=' ')

cart =[100,200,300,400,500,600,700,800,900]
purchase=[]
for i in cart:
    if i > 600:
        purchase.append(i)
        break
    else:
        print(i," is less than 600")
print ("Congratulations you have purchased ",purchase)