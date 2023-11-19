#write a program to add two matrix and save it in another matrix
import numpy as np
matrix=[]
row2=int(input("enter the row size:"))
col2=int(input("enter the col size:"))
print("Enter {} elements for matrix1".format(row2*col2))
for i in range(0,row2):
    a=[]
    for j in range(0,col2):
        a.append(int(input()))
    matrix.append(a)
# print(matrix)

matrix2=[]
print("Enter {} elements for matrix2".format(row2*col2))
for i in range(0,row2):
    a=[]
    for j in range(0,col2):
        a.append(int(input()))
    matrix2.append(a)
# print(matrix2)

matrix3=[]
for i in range(0,row2):
    a=[]
    for j in range(0,col2):
        a.append(matrix[i][j]+matrix2[i][j])
    matrix3.append(a)
mat=np.array(matrix3)
print(mat)
print("transpose of matrix is")
matrix4=[]
for i in range(0,row2):
    a=[]
    for j in range(0,col2):
        a.append(matrix3[j][i])
    matrix4.append(a)
mat2=np.array(matrix4)
print(mat2)