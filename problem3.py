# Library Borrow Checker ----Abhishek Verma
with open("library.txt","w") as f:
    d={"The God of Small Things":5,"Midnight’s Children":6,"Malgudi Days":8, "Train to Pakistan":4,"The White Tiger":2, "A Suitable Boy":3, "The Palace of Illusions":0, "Interpreter of Maladies":9, "The Inheritance of Loss":6, "Gitanjali":5}
    for key ,value in d.items():
        f.write(f"{key}:{value}\n") 
with open("library.txt","r") as f:
    data=f.read()
    print(data)               
name=input("enter the book name you want:")
val=d[name]#gives the value of the key
if val==0:
    print("out of stock")
elif val>0:
    con=input("do you want to issue the book yes or no:")
    if con=="yes":
        d[name]=val-1#updating the dictionery with new value
        print("Issued ")
with open("library.txt", "w") as f:
    for key, value in d.items():
        f.write(f"{key}: {value}\n") # writing to a txt file        

 
        

    