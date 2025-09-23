# Top-Scoring Students by Subject using csv (comma-separated values) file ----Abhishek Verma
import pandas as pd
data={"Roll.no":[101,102,103,104,105,106,107,108],
      "Name":["Alisa","Radha","shiva","Ravi","Anuj","Ram","Manish","Sapna"],
      "Math":[88,92,94,89,90,84,82,85],
     "Science":[78,98,78,88,96,67,87,87],
     "English":[86,87,78,98,67,89,78,88]}
df=pd.DataFrame(data)
df.to_csv("student.csv",index=False)
info=pd.read_csv("student.csv")
math=info["Math"]
science=info["Science"]
english=info["English"]
name=info["Name"]
id=info["Roll.no"]
m= math.max()          
ind = math.idxmax()     
m1 = name[ind] 
m2=id[ind]
s=science.max()
ind1=science.idxmax()
s1=name[ind1]
s2=id[ind1]
e=english.max()
ind2=english.idxmax()
e1=name[ind2]
e2=id[ind2]
print(s2,"Science",s1,s)
print(m2,"Math",m1,m)
print(e2,"English",e1,e)
 
    
      
    
    
    