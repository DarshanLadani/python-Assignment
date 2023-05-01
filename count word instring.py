s=input("Enter String : ")
print(s)
l=s.split()
d={}
sum=1
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=sum
print(d)
