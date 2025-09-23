#Student Attendance Manager ---Abhishek Verma
with open("attendence.txt","w") as f:
    l=["2501\n","2502\n","2503\n","2504\n","2505\n","2506\n","2507\n","2508\n","2509\n","2510\n"]
    f.writelines(l)
with open("attendence.txt","r") as f:
    roll=f.readlines() 
    l2=[]
    for i in roll:
        print(i,end="")
        att=input("P/A:")
        if att=="A":
            l2.append(i+"\n")
with open("Absent.txt","w") as f:
    f.writelines(l2)
with open("Absent.txt","r") as f:
    roll=f.read()  
    print("Absent Students are :") 
    print(roll,end="")  
    
    
               
            
        
         
    