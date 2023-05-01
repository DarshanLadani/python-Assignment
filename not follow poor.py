#Write a Python program to find the first appearance of the substring
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
#whole 'not'...'poor' substring with 'good'. Return the resulting string.

s=input("Enter string : ")
a=("not")
b=("poor")
c=(s.find("not"))
print(c)
d=(s.find("poor"))
print(d)

if a and b in s:
    if d-c==4:
        print(s.replace("not poor","good"))
    else:
        print("No Changes : ",s)
else:
    print("No Changes : ",s)
