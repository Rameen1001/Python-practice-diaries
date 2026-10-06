# while loop numbers from 1 to 10
i=1
while(i<=10):
    print(i)
    i=i+1
# keep asking password until correct
password="123456"
while True:
    pswrd=input("Enter password")
    if(pswrd==password):
        break
# reverse given number
num=123
while(num>0):
    r=num%10
    num=num//10
    print(r,end="")
print("\n")
# break statement use
for i in range(1,11):
    if(i==7):
        break
    print(i)
print("/n")
# continue statement
for i in range(1,11):
    if (i==5):
        continue
    print(i)
print("/n")
# pass statement
for i in range(1,6):
    if(i==3):
        pass
    print(i)
    

