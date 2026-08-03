# print("hello")
# def f1():
#     print("hello")

# f1()    

# a=23
# b=45
# print(a+b)

# def sum(a,b):
#     print(a+b)
    
# sum(23,45)    
# sum(10,3)

# def sum(a,b):
#     return a+b
# print(sum(12,34))

# #find sq of a no.
# def sq(a):
#     print(a*a)
# sq(5)    
  
  
# def sq(a):
#     return(a*a)
# print(sq(7))    


# #find even odd
# def even(a):
#     if a%2==0:
#         print("even") 
#     else:
#         print("odd")
# even(4)            
       
# #types of arguments
# #default
# def multi(a,b=1):
#     print(a*b)
# multi(4)           



# def multi(a,b):
#     print(a*b)
# multi(5,3)



# #keywoard arguments
# def f1(fname,lname):
#     print("fname=",fname,"lname=",lname)
# f1(fname="nikhil",lname="sharma")
# f1(lname="sharma",fname="nikhil")    


# #positional argument
# def f1(fname,lname):
#     print("fname=",fname,"lname=",lname)
# f1("nikhil","sharma")
# f1("sharma","nikhil")    
    



# #palindrome
# def h(n):
#     print (n==n[::-1])
# h("ngj")    

# #rev a string
# def j(n):
#     print(n[::-1])
# j("khj")    

# #count ch in a string 
# def count(s,char):
#     print(s.count(char))
# count("hello","l")    

# #to check if no is positive or neg
# def check(n):
#     if n>0:
#         print("postive")
#     elif n<0:
#         print("negative")
#     else:
#         print("zero")
# check(56)                
        
        
# #find largest no in list
# a=[2,4,3]
# def f1(a):
#     largest=a[0]
#     for i in a:
#         if i>largest:
#             largest=i
#     return largest
# print(f1(a))
        
        
# #count vowel in a string 
# def f1(s):
#     count=0
#     vowel="AEIOUaeiou"
#     for i in s:

#         if i in vowel:
#             count+=1
#     return count
# print(f1("sUEhfwoa"))  


# #function within function
# def f1():
#     s="Thats great"
    
#     def f2():
#         print(s)
#     f2()
# f1()    


# #anonymous funtion (lambda)

# f2=lambda x:x*x
# print(f2(2))

# g2=lambda a,b:a if a>b else b
# print(g2(4,5))

# #deference between return and print
# def sq(x):
#     return x**2
# print(sq(3))
# x=sq(2)
# y=sq(5)
# print(x+y)        #if we want to return something we use return
#                 #if we want just to show values and dont want to return 
#                 #anything we use print
# # def sq(x):
# #     print( x**2)
# # sq(3)
# # x=sq(2)
# # print(x)
# # y=sq(5)
# # print(x+y)

# def sum(a,b):
#     return a+b
# print (sum(2,3))

# def sum(a,b):
#     print(a+b)
# x=sum(2,3)
# print(x)
# y=sum(3,4)

# #recursive functions
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(3))    


# #print no 1 to 5 using recursion
# def p1(n):
#     if (n==0):
    
#        return 
#     p1(n-1)
#     print(n)
# p1(5)        

#sum(1 to n using recursion)
def sum(n):
    if n<=0:
        return 0
    return n+sum(n-1)
print(sum(10))



#globel and local scope

#local
def f1():
    s="hello"
    print("insite : ",s)
f1()    
#print("outside:",s)

#globel
s="hello"
def f2():
    print("inside",s)
f2()
print("outside",s)
  
#overwrite
def f1():
    s="hey"
    print(s)
s="fun"
f1()
print(s)  

# def f1():
#     s+="hi"
#     print(s)
# s="hello"
# f1()

#modifing global inside a function
s="hello"
def f1():
    global s
    s+="hi"
    print(s)
    s="fun"
    print(s)
f1()
print(s)

#
a=1
def f1():
    print("f1:",a)
def f2():
    a=2
    print("f2:",a)
def f3():
    global a
    a=3
    print("f3:",a)
print("global:",a)
f1()
print("global:",a)
f2()
print("global:",a)
f3()
print("global:",a)

# #fibonnaci series using recursion
# def fibo(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(5))

# for i in range(10):
#     print(fibo(i),end=" ")   
    
#fact using lambda  
# lambda_fact =lambda i:1 if i==0 else i*lambda_fact(i-1)
# print("factorial is :",lambda_fact(4))


#map function
d=[1,2,34,5]
result=[]
for i in d:
    result.append(i*2)
print(result)

print(list(map(lambda x:x*2,d)))


f1=["1","2","3","4"]
print(list(map(int,f1)))

g=[2,3,4,5]
print(list(map(lambda x:x**2,g)))

a=[3,4,56,7]
s=[3,4,6,34]
print(list(map(lambda c,s:c+s,a,s)))


w=["wegfu","bhvj"]
print(list(map(str.upper,w)))

print(list(map(lambda s:s[0],w)))


w=["  wegfu  ","  bhvj  "]
print(list(map(str.strip,w)))


tmp=[0,56,45]
print(list(map(lambda x:9/5*x+32,tmp)))

#finish map function

        
#reduce 
from functools import reduce 
a=[2,3,8,5,6,7]
print(reduce(lambda x,y:x+y,a))

s=["hello","hi",]
print(reduce(lambda x,y:x+" "+y,s))

print(reduce(lambda  x,y:x if x>y else y,a))

from itertools import accumulate
from operator import add
print(list(accumulate(a,add)))


#filter function 

c=["asdf","hi","hello","anime"] 
def f1(w):
    return w.startswith("a")
print(list(filter(f1,c)))   
    

ev=[2,3,4,5,6]  
def f1(n):
    return n%2==0
        
print(list(filter(f1,ev)))        
        
    
        
#divisible by three
dc=[3,4,5,6,7,8,8,15,18]
def f1(n):
    return n%3==0
print(list(filter(f1,dc)))    
    
#words longer then 5 letters
dg=["sg","sagrha","dfhqdwj","gjk"]
def f1(n):
    return len(n)>5
print(list(filter(f1,dg)))
    
        
#remove falsy values
de=["jdsf"," ",2,45,"","sdn"]    
print(list(filter(bool,de)))



























