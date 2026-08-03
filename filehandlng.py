# f=open("sample.txt","r")
# data=f.read(12)
# print(data)

# print(type(data))

# f.close()


# f=open("sample.txt","r")
# data=f.readline()
# data2=f.readline()
# print(data)
# print(data2)
# print(type(data))

# f.close()


# f=open("sample.txt","r")
# data=f.read()

# print(data)
# line=f.readline()
# print(line)
# print(type(data))

# f.close()


# f=open("sample1.txt","w")
# data=f.write(" this is a write mode file")

# f.close()

# f=open("sample.txt","a")
# data=f.write("\n hello")

# f.close()


# f=open("sample.txt","a")
# data=f.write("hey")


# f=open("sample1.txt","r+")
# f.write("yup")
# print(f.read())

# f=open("sample1.txt","w+")
# f.write("whatsap")
# f.close()



# f=open("sample1.txt","a+")
# print(f.read())
# f.write("hello")
# f.close()


# with open("sample1.txt","r") as f:
#     data=f.read()
#     print(data)
    

# with open("sample1.txt","w") as f:
#     f.write("already")
    
    
# import os
# os.remove("sample.txt")


with open("practice.txt","w") as f:
    f.write("hi everyone\ni m learning file os\nusing python\ni like programming in python")


with open("practice.txt","r") as f:
    data=f.read()
    
newdata=data.replace("python","c++")
print(data)
    
with open("practice.txt","w")as f:
    f.write(newdata)


with open("practice.txt","r")as f:
    data=f.read()
    if (data.find("learning")!=-1):
        print("found")
    else:print("not found")

