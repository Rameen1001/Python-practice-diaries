try:
    num=int(input("enter a number"))
except:
    print("not an integer")
try:
    num/0
except:
    print("division by zero")