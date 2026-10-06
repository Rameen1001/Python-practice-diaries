import sys
'''try:
    print("Basic arithmatic calculator")
    v1 =float(input("First number"))
    op= input("choose the operation you want to perform,(+,-,*/)")
    v2= float(input("second number"))



    if op == "+":
       result = v1+v2
    elif op== "*":
        result =v1*v2
    elif op == "/":
       if v2 ==0:
           print("cannot divide by 0")
           sys.exit()
           
       else:  
           result=v1/v2
          
    elif op== "-":
       result = v1-v2
    else:
        print("something went wrong")

    print(result)
except SystemExit:
    pass
except:
    print("wait for update")'''





print("                                                             calcultor")

'''def add(x,y):
    return(x+y)
def substrect(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    if y==0:
       print("cannot divide by 0")
       sys.exit()
    return(x / y)

try:
    v1 = float(input("first value"))
    op = input("choose one of the following (+,-,*,/)")
    v2 = float(input("second value"))
    if op== "+":
       result = add(v1,v2)
    elif op== "-":
       result = substrect(v1,v2)
    elif op == "*":
       result =multiply(v1,v2)
    elif op=="/":
        result= divide(v1,v2)
    print(f"the result is {result}")
except SystemExit:
    pass
except:
    print("Please type numbers only")
'''
print(" ")
print("                                                  celcius to fahrenheit and vice versa")
'''print("1:Celcuis to fahrenheit")
print("2:fahrenheit to celcius")


def ctof(a):
    return((a*9/5)+32)
def ftoc(a):
    return((a-32)*5/9)
choice = float(input("type option number:1 or 2"))
t= float(input("enter t to convert"))
if choice== 1:
   result =ctof(t)
if choice== 2:
   result = ftoc(t)
print(result)'''

   
print("                                                          Area of triangle")

'''def area(a,b):
    return(0.5*a*b)
print("To calculate the area of triangle we need the length of base and height.")
try:
    base =float(input("type the base of triangle"))


    height = float(input("type the height of triangle"))
    result =area(base,height)
    print(f"The area of given triangle is {result}")
except ValueError:
    print("type numbers only")'''



print("                                                           swap variables")

'''a = input("first variable a:")
b = input("second variable b:")
print(f"orignal values a = {a} and b = {b}")
c = a
a = b
b = c
print(f" swapped vlues: a = {a} and b =  {b}")'''



print("                                                           random numberr")
'''import random
print(f"randum number : {random.randint(1,100)}")'''




print("                                                              calander")

import calendar
'''try:
    date = int(input("enter date"))
    month =int(input("enter month"))
    year = int(input("enter year"))
    day =calendar.weekday(year,month,date)
    print(calendar.day_name[day])
except ValueError:
   print("numbers only")'''


import math
print("                                                      solve quadratic equation")
'''print("the quadratic is of the form:ax^2 + bx + c=0")
print("enter the coeffients of the equation and the constant(a,b,c).")
a =float(input("enter the value of a"))
b= float(input("enter the value of b"))
c= float(input("enter the value of c"))

disc = b**2 - 4*(a*c)
print(disc)
if disc >= 0:
    root1 = (-b+ math.sqrt(disc))/2*a
    root2 = (-b- math.sqrt(disc))/2*a
    print(f"root1 is {root1}")
    print(f"root2 is{root2}")
else:
    rpart= -b/(2*a)
    ipart = math.sqrt(abs(disc))/(2*a)
    root1 = complex(rpart,ipart)
    root2 = complex(rpart -ipart)
    print(root1)
    print(root2)'''



print("                                                         even and odd numbers")

'''print("enter the number to check")
n = int(input("number:"))
if n == 0:
   print("the number is 0")
d = n%2
if d ==0:
    print(f"{n} is even")
else:
   print(f"{n} is odd")'''




print("                                                     negative or positive number")
'''n = float(input("enter the number:"))
if n == 0:
    print("the number is 0")
elif n > 0:
    print("the number is positive")
else:
    print("the number is negative")'''


print("                                                              leap year")
'''year= int(input("enter the year :"))
leap= calendar.isleap(year)
if leap == True:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")'''


print("                                                          check prime number")

'''n = int(input("enter the number :"))

if n==1:
    print(f"{n} is not prime")
elif n== 2:
    print(f"{n} is prime")
else:
    for i in range(2, int(math.sqrt(n)) +1):
        r =n%i
        if r == 0:
            print(f"{n} is not prime")
            break
        else:
            print(f"{n} is prime")'''
    


print("                                                prime and not prime lists in given range ")
'''n = int(input("enter the number :"))
primelist= []
notprimelist= []
for n in range(1,n+1):
    if n==1:
        notprimelist.append(n)
    elif n== 2:
        primelist.append(n)
    else:
        for i in range(2, int(math.sqrt(n)) +1):
            r =n%i
            if r == 0:
                notprimelist.append(n)
                break
        else:
            primelist.append(n)
print(f"The list below containns all the prime numbers from 1 to {n}")
print(primelist)
print(f"The list below contains all the numbers from 1 to {n} which are not prime")
print(notprimelist)'''



print("                                                         multiplication table")

'''n= int(input("Enter the number to get its multiplication table"))

for i in range(1,11):
    print(f"{n} {i} times = {n*i}")'''




print("                                                      find factorial of a number")

'''n = int(input("enter the number to find its factorial"))
f=1
if n ==0:
    print("The factorial of 0 is one.")
elif n< 0:
    print(F"{n} has no factorial.")
else:
    for i in range(1,n+1):

        f =f*i
    
    print(f"The factorial of {n} is {f}")
'''


print("                                                         fibonaccis sequence")
'''f = [0,1]
value = int(input("enter the numberr"))
fseq=2
if value==0:
    print(0)

else:
    for i in range(fseq,value):
        sequence= f[-1] +f[-2]
        f.append(sequence)
    for x in f:
        print(x)'''



print("                                                            Arm's strong")
'''value= int(input("value"))

for a in range(1,value+1):
    total = 0
    strng = str(a)
    l = len(strng)
    
    for i in strng:
        srt = int(i)**l
        
        total += srt
    
    if total == a:
        print(a)'''




print("                                                         sum of a given range")

'''value = int(input("value"))
total = 0
for i in range(1,value+1):
    total += i
print(total)'''



print("                                                                 LCM")
'''
listlcm= []

value1 = int(input("enter the first number"))
value2 =int(input("enter the second number"))
i =1
while True:
    if i %value1 ==0 and i% value2==0:
        print(i)
        break
    i+= 1'''



print("                                                                 HCF")


'''i =  1

list_hcf =[]
value1 =int(input("enter the first value"))
value2 =int(input("enter the second value"))

if value1> value2:
    greater = value1
else:
      greater = value2
for i in range(1,greater):
    if value1%i ==0 and value2%i==0:
        list_hcf.append(i)
print(list_hcf[-1])'''
        
    