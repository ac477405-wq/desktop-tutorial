s=input("enter the numbers with space:")
l=s.split( )
th=int(input("enter threshold:"))
list=[]
for i in l:
    j=int(i)
    if j<th:
        n=l.index(i)
        list.append(n)
print(list)