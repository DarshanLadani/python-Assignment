s1=input("Enter String 1 :")
s2=input("Enter String 2 :")
temp=s1[0:2]
print(s1,s2)
s1=s1.replace(s1[0:2],s2[0:2])
s2=s2.replace(s2[0:2],temp)

print(s1,s2)

    
    
