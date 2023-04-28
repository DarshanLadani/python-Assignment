s=input("Enter String : ")

if len(s)>2:
    if s.endswith("ing"):
        print(s+"ly")
    else:
        print(s+"ing")
else:
    print("!!!! Enter String More Then 2 Characters !!!!")
    
    
