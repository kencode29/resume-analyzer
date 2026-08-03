a=["sdf","gfh",4,True]
b=list("hfj")
print(b)
print(a[1:7])
print(a[3:10])
print(a[2:9])
print(a[-1:])
print(a[-1:-3:-1])
print(a[1:4:2])
print(a[:-4:-2])
print(a[3])
print(a[-2])
print(a[2])


#elements adding
a.append(5)
print(a)
a.insert(2,6)
print(a)
a.extend([7,8,9,7])
print(a)
a.append(34)
print(a)
a.insert(5,67)
print(a)
a.extend(["jk",87])
print(a)
a.remove("jk")
print(a)

a[1]=0
print(a)

#delete
del a[0]
print(a)

a.remove(7)
print(a)

n=a.pop(1)
print(n)

a.pop()
print(a)
a.clear()
print(a)

b=["jhf","juiw",5,82,54,3,6]
print(b)

b.remove(3)
print(b)

del b[3]
print(b)

b.pop()
print(b)

n=b.pop(3)
print(n)

#iteration

for i in b:
   print(i)

#nested lists

c=[1,2,[3,4]]
print(c[2][0])

h=[1,2,[3,[4,5]]]
print(h[2][1][1])

l=[1,[2,3],4,[5,[6,[7,8]]]]
print(l[3][1][1][1])

o=[[1,2],3,[4,[5,6,[7,8]]]]
print(o[2][1][2][1])