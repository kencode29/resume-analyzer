import numpy as np  #here np is in short numpy
a=[1,2,3,4,5]   #if we put any other datatype in list the              it automatically
                #convert the whole list into that datatype
                #we can also change datatype into other datatype 
                # by using dtyping as below given  
array1=np.array(a,dtype=float)
print(array1)
print(type(array1))

#1d array=list 

#2d array

a=[[1,2,3],[4,5,6],[7,8,9]]
array1=np.array(a)
print(array1)

a=np.arange(1,8)
print(a)

a=np.arange(11,17).reshape(2,3)
print(a)

a=np.zeros(4)
print(a)

a=np.ones(4)
print(a)


''' attributes of numpy array
1)ndim
2)shape
3)size
4)dtype
5)itemsize  '''

l=[1,2,3,4]
a=np.array(l)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)



l=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(l)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)


#indexing in array
l=[1,2,3,4,5]
a=np.array(l)
print(a[0])
print(a[-1])

l=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(l)
print(a[1,2])
print(a[0,:])
print(a[:,1])
print("---------------------------")
#  slicing
l=[1,2,3,4,5,6,7,8,9]
a=np.array(l)
print()
print(a[1:3])
print(a[1:6:2])
print(a[::2])
print(a[::-1])
print(a[-1:-3:-1  ])

print("---------------------------")

a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a[1,])   #1st whole row 
                #here we can leave the 2nd place blank it will be no prob
                #we also can put : in 2nd place
print(a[:,1]) #1st row whole column
                #here we can leave the 1st one blank we have to put : in there otherwise it will show error 
print(a[1:3 , 1:3]) #row range, columnn range
print(a[1:3 , ]) #row range
print(a[:, 1:3])  #column range
print(a[1:3,1])   #1,2 - row ; 1st column
print(a[1:3,:1])    #1,2 - row ; stop bit-1 sp 0th column

print("---------------------------")


lspace=np.linspace(1,4,4)
print(lspace)

emp=np.empty((3,4))
print(emp)
emp[0,1]=10
print(emp)
emp[0]=[1,2,3,4]
print(emp)


ide=np.identity(3)
print(ide)
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a.T)

for i in a.flat:
    print(i)
    
marks=np.array([[3,4,5],
            [1,4,7],
            [6,8,9]])    
print(np.where(marks>4))
print(np.unique(marks))
print(np.argmax(marks,axis=0))
print(np.count_nonzero(marks))


from array import *
vals=array("i",[5,8,9,3,4])
print(vals)
vals=array("f",[5.7,8,9,3,4])
print(vals)
vals=array("i",[5,-8,9,3,4])
print(vals)
# vals=array("I",[5,-8,9,3,4])
# print(vals)

#dynamic array
a=array("i",[])
n=int(input("enter length of array :"))
for i in range(n):
    x=int(input("enter elements of array : "))
    a.append(x)
    print(a)
    
#if we try to run this same code in 2-d it cannot do that , so numpy

# vals=array("i",[2,3],[4,5],[6,7])
# print(vals)

#vectorization 
marks=[85,82,90]
result=[]
for i in marks:
    result.append(i+5)
    print(result)
    
import numpy as np 
marks=np.array([85,82,90])
new_marks=marks+5
print(new_marks)


#question = write a program to find the sum of diagonal elements of matrix using numpy

row=int(input("enter row:"))
column=int(input("enter columns:"))
c=np.zeros((row,column))
print(c)

for i in range(row):
    for j in range(column):
        c[i][j]=int(input("enter element :"))
print("matrix :")
print(c)


diagonal_sum=0
for i in range(row):
    for j in range(column):
        if i==j:
            diagonal_sum+=c[i][j]
            
print("sum of diagonal elements=",diagonal_sum)
         
#finished