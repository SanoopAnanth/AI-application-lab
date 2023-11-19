# write a python program to implement list operations(nested list, length, concatenation, membership, iteration,indexing and slicing)
l=[["boost","coffee","bread"]]
x=[["idly","dosa","pongal","puri"],["rice","pulaw","chappati"],["rice","curd rice","chappati"]]
print(x)
print("Length of list is {}".format(len(x)))
print("printing elements in list")
for i in x:
    for j in i:
        print(j)
    print()
print("Concatination of list")
# x.extend(l)
my_li1=["a","b","c","d"]
my_li2=["e","f","g","h"]
print(my_li1+my_li2)
print("getting 1st element in my_li1 using indexing")
print(my_li1[1])
print("Slicig through first 2 elements in a list")
print(my_li1[0:2])
