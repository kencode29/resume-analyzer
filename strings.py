#strings
a="jsbdjk"
print(type(a))

b=84736
print(type(b))

c=7.42
print(type(c))

#indexing
print(a[0])
#neg. indexing
print(a[-6])

#slicing
print(a[1:5])
print(a[:5])
print(a[1:])
print(a[:])

#ex of slice
k="lksndl"
print(k[3:5])
print(k[:5])
print(k[3:])
print(k[::2])
print(k[::-2])

#iteration
for i in k:
    print(i)
for i in a:
    print(a)    
    
h="fqwvchj"
for i in h:
    print(h)   
     
#immutable
h="F"+h[1:]
print(h)

del h
#print(h)

#update
a=a.replace("bdjk","l")
print(a)

print(a.upper())
a="   HHJ  HJ   "
b=a.strip()
print(len(a))

print(a.lower())
s="fjfd"
print(b+" "+s)
print(b*3)

#formatting
name="gdx"
print(f"my name is {name}")

print("my anme is {}".format("gdx"))