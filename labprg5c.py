import numpy as np
matrix=[]
row1=int(input("enter the row size:"))
col1=int(input("enter the col size:"))
print("Enter {} elements for matrix1".format(row1*col1))
for i in range(0,row1):
    a=[]
    for j in range(0,col1):
        a.append(int(input()))
    matrix.append(a)
# print(matrix)

matrix2=[]
row2=int(input("enter the row size:"))
col2=int(input("enter the col size:"))
print("Enter {} elements for matrix2".format(row2*col2))
for i in range(0,row2):
    a=[]
    for j in range(0,col2):
        a.append(int(input()))
    matrix2.append(a)
# print(matrix2)

ma1=np.array(matrix)
ma2=np.array(matrix2)
if col1==row2:
    result=np.dot(ma1,ma2)
    print(result)
else:
    print("Multiplication not possible")
