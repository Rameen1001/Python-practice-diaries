n=0
min=0
max=0
m=0
count=0
while(True):
    num=int(input("Enter number"))
    if(num>max):
        m=num
    if(num<min):
        n=num
    count=count+1
    if num==-1:
        break
print("total numbers",count)
print("largest number", m)
print("smallest number", n)

    
    
