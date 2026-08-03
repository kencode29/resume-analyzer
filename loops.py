# print even no from 1 to 50
# print odd no from 1 to 50


#  for i in range(2,51,2):
#      print(i)
    
# sum from 1 to 100
# sum=0 
# for i in range(1,101):
#     sum+=i
# print(sum)


# #1 to 100 divide by 5
# a=0
# for i in range(1,100):
#     if i%5==0:
#         a=a+1
# print(i)
      
      
        
# b=0
# for i in range(1,50):
#     if i%5==0:
#         a=a+1
# print(i)


# n=10
# sum=0        
# for i in range(1,n):
#     sum+=i
# print(sum)   

     
           
# n=1
# for i in range (1,6):
#    n=n*i 
# print(n)



# # f=int(input("enter any no: "))
# # factorial=1
# # for i in range(1,f+1):
# #     factorial=factorial*i
# # print(factorial)



# while loop
# i =1
# while i <=10:
#     print(i)
#     i=i+1

# i=10
# while i>=1:
#     print(i)
#     i=i-1

#sum from 1 to n
# n=10
# sum=0
# i=1
# while i<=n:
    
#     sum+=i
#     i+=1
# print(sum)

# #mutliples of three 
# i=3 
# while i<=30:
#     print(i)    
#     i+=3

# #reverse a no
# a=1234
# b=str(a)
# print(b[::-1])

# a="jshgk"
# b=str(a)
# print(b[::-1])

     
# #nested loops

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
        
        
# for i in range(1,5):
#     for j in range(i):
#         print(i,end=" ")
#     print()        
    
    
# for i in range (4,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()        
                
 

# while n!=0:
#     n=int(input("enter your number: "))

# n=0
# while not (1<=n<=100):   
#     n=int(input("enter a no between 1 to 100: "))
# print("your no is :",n)    


#loop control statements

#continue:skip
for i in "papaya":
    if i=="a":
        continue
    print(i)
    
    
#break:bring control out o f loop    
for i in "papaya":
    if i=="a":
        break
    print(i)  
    
#pass:similar to continue but we have to put else in this    
for i in "papaya":
    if i=="a":
        pass
    else:
        print(i)    
        
        
# #calculator
# while True:
#     print("press 1 for plus")
#     print("press 2 for minus")
#     print("press 3 for multiply")
#     print("press 4 for divide")
#     print("press 5 for exit ")

#     b=int(input("enter your choice :"))
#     if b==5:
#         print("Calc closed")
#         break
    
#     if b in [1,2,3,4]:
#         num1=float(input("enter the value for first value: "))
#         num2=float(input("enter the value for second value "))

#     if b==1:
#         print(num1+num2)
#     elif b==2:
#         print(num1-num2)
#     elif b==3:
#         print(num1*num2)
#     elif b==4:
#         if num2!=0:
#             print(num1/num2)
#         else:
#             print("nuber can't be divided by zero")           
#     else:
#         print("invalid number ! try again ")
  
        
#     again=input("do u want to use calculator again? (yes/no)")
#     print()
#     if again.lower() !="yes":
#         print("calc closed")
#         break       

        