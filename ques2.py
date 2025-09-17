num=input("enter the numbers with space:")
list=num.split( )
s=set(list)
n=0
l=len(list)
if len(s)==5:
    while n<l-1:
        if list[n]==list[n+1]: 
            print("False")  
            break   
        elif list[n]!=list[n+1]:
            n+=1 
    if n==(l-1):       
        print("true")
elif len(s)!=5:
    print("False")    
        
        
