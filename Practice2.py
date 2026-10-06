# if else statements "positive or negative"

no=int(input("enter a number"))
if(no>0):
    print("number is positive")
elif(no<0):
    print("number is negative")
else:
    print("number is zero")
# Checks eligibility for vote

age=int(input("enter your age"))
if(age>18):
    print("You are eligible for vote")
else:
    print("you are not eligible for vote")
# Even or Odd

num=int(input("enter a number"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")
# Match case statements "day number"

day_num=int(input("Enter day number"))
match day_num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("invalid day number")
 # match case calculator

num1=int(input("Enter 1st number"))
num2=int(input("enter 2nd number"))
op=input("Enter operator(+,-,/ *)")
match op:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "/":
        print(num1/num2)
    case "*":
        print(num1*num2)
    case _:
        print("invalid operator")
# For loops 1 to 10 counting

for i in range (1, 11):
    print(i)
# multiplication table

tab_num=int(input("Enter table no"))
for i in range(1, 11):
    print(tab_num,"*",i ,"=",tab_num*i)
# Sum of numbers from 1 to 100

sum=0
for i in range(1,101):
    sum= sum+i
print(sum)
# pattern using for loop

for i in range(1,5):
    print("*"*i)

    






