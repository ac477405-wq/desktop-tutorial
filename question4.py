st=input("enter the strings with space:")
li=st.split( )
list=[]
for i in li:
    j=i[-1::-1]
    if i==j:
        list.append("true")
    else:
        list.append("false")    
print(list)        