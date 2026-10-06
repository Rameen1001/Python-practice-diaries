sen="No Melon,no lemon"
sen=sen.replace(",","").replace("!","").replace(" ","")
sen=(sen.lower())
print (sen)
reverse=sen[::-1]
if sen==reverse:
    print("sen is palidrome")
else:
    print("its not")