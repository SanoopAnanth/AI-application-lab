# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number: "))
a=factorial(n)
print(a)