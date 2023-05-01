s=input("Enter String")
d={}
sum=1
for i in s:
    if i in d :
        d[i]=sum+1
    else:
        d[i]=sum
print(d)
        
