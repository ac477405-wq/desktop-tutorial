# Word Frequency Filter-----Abhishek Verma
import string
with open("story.txt","w") as f:
    f.write("One day, a boy had a ball. The boy liked the ball. The boy played with the ball again and again. The ball bounced high, the ball bounced low, the ball bounced fast, the ball bounced slow. The boy threw the ball, the boy caught the ball, the boy lost the ball, then the boy found the ball. The ball made the boy happy, and the boy made the ball busy. The boy and the ball, the ball and the boy, stayed together all day.")
with open("story.txt","r") as f:
    a=f.read()
    n=int(input("enter the min word frequency:"))
    for p in string.punctuation:
        a = a.replace(p, "")
    l=a.split(" ")
    s=set(l)
    for i in s:
        n1=l.count(i)
        if n1>=n:
            print(i,":",n1)    