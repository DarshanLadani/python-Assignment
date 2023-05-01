s=input("Enter string : ")
s=s.split()
print(s)
temp=0
for i in s:
    for j in s:
         if(len(i)<len(j)):
            temp=i
            i=j
            j=temp
print("Longest word is :" i)
            
            
