# x=int(input("enter the number:  "))
# for i in range(1,x+1):
#     for x in range(1,11):
#         print("{multiplier} x {multiplicand} = {resu}".format(multiplier=i,multiplicand=x,resu=x*i))
#     print("\n")
num=int(input("enter the number: "))
for i in range(1,num+1):
    for x in range(1,11):
        print(str(i)+"x"+str(x)+"="+str(i*x))
    print()