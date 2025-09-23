#Unique Numbers & Statistics -----Abhishek Verma
n=input(" enter the number with space:")
l=n.split(" ")
s=set(l)
c=len(s)
print("total unique no is :",c)
sum=0
l2=[]
for i in l:
    j=int(i)
    l2.append(j)
    sum+=j
print("sum=",sum)
no=len(l)
print("average is ",sum/no)
ma=max(l2)
mi=min(l2)
print("minimum",mi)
print("maximum",ma)




