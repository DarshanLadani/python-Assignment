s=input("Enter string : ")
b=s.capitalize
a=len(s)
if a%4==0:
    print(s[::-1])
else:
    print("No Changes : ",s)
