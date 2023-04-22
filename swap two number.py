a=int(input(" Enter Value 1 : "))
b=int(input(" Enter Value 2 : "))
temp=0
temp=a
a=b
b=temp
print(" After Swaping with temp ")
print(" Value 1 : ",a)
print(" Value 2 : ",b)

x=int(input(" Enter Value 1 : "))
y=int(input(" Enter Value 2 : "))
print(" After Swaping without temp ")
x=y+x
y=x-y
x=x-y

print(" Value 1 : ",x)
print(" Value 2 : ",y)
