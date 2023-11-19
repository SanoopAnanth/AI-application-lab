import numpy as np
row1=int(input("enter the number of rows for 1st matrix: "))
col1=int(input("enter the number of columns for 1st matrix: "))
print("Enter {} elements".format(row1*col1))
matrix1=[]
for i in range(0,row1):
    a=[]
    for j in range(0,col1):
        a.append(int(input()))
    matrix1.append(a)
row2=int(input("enter the number of rows for 1st matrix: "))
col2=int(input("enter the number of columns for 1st matrix: "))
print("Enter {} elements".format(row2*col2))
matrix2=[]
for i in range(0,row2):
    a=[]
    for j in range(0,col2):
        a.append(int(input()))
    matrix2.append(a)
# matrix3=[]
# for i in range(0,row2):
#     a=[]
#     for j in range(0,col2):
#         a.append(matrix1[i][j]+matrix2[i][j])
#     matrix3.append(a)
# ma1=np.array(matrix3)
# print(ma1)
ma1=np.array(matrix1)
ma2=np.array(matrix2)
if col1==row2:
    result=np.dot(ma1,ma2)
    print(result)
else:
    print("Multiplication error")