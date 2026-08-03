import random 
# students=input("enter names of students :").split()
# winner=random.choice(students)
# print("Lucky Draw winner is :",winner)


import string
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

pas=int(input("Enter the length for password :"))
a=string.ascii_letters+string.digits+string.punctuation
pas1=""
for i in range(pas):
    pas1+=random.choice(a)
print("randomly generated password is :",pas1)
 