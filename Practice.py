#declaring variables
x = 1
y = "string"
a=b=c=1
d,e,f= "printing Multiple_","Variable_","Using + in between"

#printing output

print(x)
print(y)
print(a,b,c)
print(d+e+f)

# creating local variable to show the alternative outcome but the print operator's indent should 
# be equal to the new code line of declaring variable


def myfunc():
    f = "using , in between"
    print(d,e,f)
myfunc()

#printing data type

print(type(x))
print(type(y))

#typecasting
x = str(x)
print(type(x))
# y = int function cannot convert datatype of  non numeric characters to int
# string function can convert any datatype to str 
print("----------------------------------------------")

# Numbers
print("                                numbers")
# integers can be positive or negative
# flot can be positive or negative numbers with decimal or with power of ten in scientific notation
x = -9e55
print(x)
a= int(x)
# converting the datatype gives full number
print(a)
x= 5j
print(a)
#a = int(x) it will give an error as complex numbers cannot be converted to other number type
print("random module")
import random
print(random.randrange(2,6))
print("-------------------------------------------------------------")

#strings
print("                                 Strings")
# we can get the elements of a string
x = "  Apple is sweet  "
print(x[3])
# we can get each element of the string using for loop
for a in (x):
    print(a)
print("finding length in string")
print(len(x))
print("checking the pressence of a certain element")
print("Apple" in x)
print("Use of if function")

if "apple" in x:
    print("yes apple is present")

#absence of an element
if "banana" not in x:

    print("no banana is not present")
    # if the condition does not fulfilled then there will be no output
    print("------------------------------------------------")
print("                              slicing strings")
#we can get the range of characters using slice syntax
print(x[2:13])
print(x[-15:-1])
print("--------------------------------------------------------")
print("                            modifying the strings")

print(x.upper())
print(x.lower())

print("replacing the string")
a =x.replace("p", "J")
# this syntax will replace all the identical characters with the new one
print(a)
print("conversion of strings to lists using split syntax")
print(x.split(","))

print("removing spaces at the begining or the end of the string")
print(x.strip())
print("------------------------------------------------")
print("                              format strings")
# f-string allows to write the non alphabatic data and allows arithmatic operations within string
calories = 52.0
x = f"Apple is sweet and there are {calories} calories in it"
print(x)

y = f"two plus two is {2+2} four"
print(y)
print(f"A modifier can also be added like {1:.2f}")
print("------------------------------------------")
print("                                  escape characters")
# An illegal character can be escaped using 
print("My name is \"Zubair\"")
txt = "Hello World!"
txt = "Hello \nWorld!"
print(txt)
print("--------------------------------------------")
print("                           string method")
# There are built in methods which can be used to modify string
print("--------------------------------------------")
print("conversion of first letter of paragraph to uppercase.".capitalize())
print("conversion of all the letters to uppercase".upper())
print("CONVERSION OF ALL HE CHARACTERS TO LOWER CASE".lower())
print("CONVERSION OF ALL HE CHARACTERS TO LOWER CASE".casefold())
#the center method adds padding incase of the lingth of padding being bigger than the string length 
# only and if the string length is odd number then it adds to the right side
print("   adding space before and after the strinng   ".center(48,"o"))
print("counting the number of a word occured in a string".count("a",0,45))#end and start values can be added
print("checking if the string ends with the specified value.".endswith(("value.",".")))#end and start values can be added
#to check with multiples values double paranthesis are required
print("expandtabs \t sets \t the \t spacesize \t of \t tab".expandtabs(10))
print(".find helps to find the location of a certain value".find("location"))
print("there are more then {:.2f}methods to format string".format(1))
print("A string can be checked if it contain alphanumeric characters only".isalnum())
#space is not alphanumeric so the result is false
print("checking if the characters are alphabets only".isalpha())# this is also false because of space
print("34343434".isascii())
print("23332".isdecimal()) #does not work with other numwral systems
print("345".isdigit())#works with other numeral systems
print("234".isnumeric())
print("abcdefg".isidentifier())# identifier does not conntain spaces and does not start with a number
print("checking if all the alphabets are in lower form .this method ignores numbers, spaces etc.".islower())
print("lets check if all the characters are printable".isprintable())#\n line break is notprintable so it will return false
print("  ".isspace())# true if there is nothinng besides space in the string
print("Checking If This Is A Title Or Not".istitle()) # a title's every word's first letter is always upper and rest always lower.
#this method ignores numbers and symbols
print("CHECKING IF ALL THE CHARACTERS ARE UPPER ONLY".isupper())# this method checks the alphabets
jointuple=("Joining","the","elements","of","a","tuple") # join method can make a string from tuple
print("-".join(jointuple))# in case of a dictionary only the keys will show up not the values
print("addind padding and left alligning the text".ljust(77,"a"))
print("CONVERTING THE LETTERS TO lowercase".lower())
print("             stripping spaces from left side of the       string".lstrip())# we can remove other characters by setting the parameter
print("dividing the string into parts before and after the specified word".partition("parts"))
print("changing a word with another word".replace("changing","replacing")) # number of replacements can be set
print("finding a word's most right position of all the position 's".rfind("position"))
print("finding the most right position from all the position using index method".rindex("position"))
print("spliting the , string, at specified, characters, or symbols".split(","))
print("addding paddint and right alligning the string".rjust(65,"#"))
print("making partitions but the partions happen  at the last occurence of value".rpartition("partions"))
print("spliting,the,string,starting ,from,right".rsplit(",",2))
print("removing spaces or specified character from right side of string ooooooooo".rstrip("o"))
print("splitting, the , string, in, parts".split(","))
print("splitting multiline \n string into \n list at each \n linebreak".splitlines(False))# by putting True it will show \n
print("checking if the string starts with a specific value".startswith(("checking","if")))
print("removing spaces and specified characters from the sides      ,.,.,,..,".strip(" ,."))
print("converting from UPPER to LOWER and viceversa SIMULTANEOUSLY".swapcase())
print("converting each word's first letter to upper to make title".title())
e="Apple"
f="Mango"
g= str.maketrans(e,f)
print(x.translate(g))
print("converting the string to uppercase".upper())
print("filling the string to reach a specific length".zfill(80))
print("--------------------------------------------------------")
print("                                                                  Booleans")

print(10>5)
def myfunc():
    x= 5
    y= 10
    if x<y:
        print("yes")
    else:
        print("no")
myfunc()
print("--------------------------------------------------------------------------")
print("                                                                  python operator")
def myfunc():
   print(x:=4)
myfunc()
print("                                                                  lists")
print(["This is", "is a ","list."]) # changable "individual value can be modified" and can contain different data types
print(len(["This is", "is a ","list."]))
print(type(["This is", "is a ","list."]))
print(list(("making list", "using list","constructer")))
print("--------------------------------------------------------------------------")
print("                                                                 Access list items")
mylist= [" This is",  "a practice","list"]
print(mylist[1])
print(mylist[0:2])
if "list" in mylist:
    print("checking the pressence of a value in list")
print("--------------------------------------------------------------------------")
mylist[2]="list."# changing the value of a value in the list
mylist[1:3]=["a list","practice"]
print(mylist)
# value can be added and removed if the number of value beign replaced don't match with the values being changed
mylist.insert(2,"I am going to use for")# the value is added at the index provided in line of code
print(mylist)
print("--------------------------------------------------------------------------")
print("                                                                     Add list items")
list2=["adding new","values","in the"]
list2.append("list")
print(list2)
list2.extend(mylist) #adding the elements of a list into another
print(list2)
print("--------------------------------------------------------------------------")
print("                                                                    Remove list items")
mylist.remove("I am going to use for") # removing the element using its value
print(mylist)
mylist.pop(1) # removinng the element using its index
print(mylist)
del list2 # priting list2 gives error as there is no list
mylist.clear()
print(mylist)# removes all the  content from the list but list remains
print("--------------------------------------------------------------------------")
print("                                                                        loop lists")
del mylist
mylist2=[1,6,3,4,5,8,12,0]
print(mylist2)
for x in mylist2:
    print(x)
i=2
while i <len(mylist2):
    print(mylist2[i])
    i+=1
[print(x) for x in mylist2]# this method can be used for strings as well
print("--------------------------------------------------------------------------")
print("                                                              list comprehension")
lict= ["apple","Mango","grapes","kiwi","lichi"]
newlict=[]
for x in lict:
    if "a" in x:
        newlict.append(x)
print(newlict)
newlict=[x for x in lict if "a" in x]
print(newlict)
newlist=[x for x in mylist2 if x <4 ]
print(newlist)
newlist2=[-x for x in newlist]
print(newlist2)
newlist3= [x if x <5 else 2 for x in mylist2]
print(newlist3)
print("--------------------------------------------------------------------------")
print("                                                                   sort lists")
print(mylist2)
mylist2.sort()#ascendig
print(mylist2)
mylist2.sort(reverse=True)#decending
print(list)
def myfunc(n):
    return abs(n-5)
mylist2.sort(key=myfunc)
print(mylist2)
lict.sort(key=str.lower)
print(lict)
lict.reverse()
print(lict)
print("--------------------------------------------------------------------------")
print("                                                                   copy list")
list3= mylist2.copy()
print(list3)
list4=list(mylist2)
print(list4)
list5= mylist2[:]
print(list5)
print("--------------------------------------------------------------------------")
print("                                                                   join lists")
list6= list3+list4
print(list6)
del list6
for x in list3:
    list4.append(x)
print(list4)
list3.extend(list4)
print(list3)
print("--------------------------------------------------------------------------")
print("                                                                  list methods")
print(list3.count(6))
print(list4.index(12))# gives the index of the first occurence of the specified value
print("--------------------------------------------------------------------------")
print("                                                                     tuples")
tuple1=(1,2,3,4,5)
print(tuple1)
print(tuple1[2:4])
if 3 in tuple1:
    print("yes")
print("--------------------------------------------------------------------------")
print("                                                                   update tuple")
# tuples are not changable but can be converted to lists to do the necessary changes and 
print("to add new items in tuple you can add tuple to tuple or conver it to list to add items.")
listtuple=list(tuple1)       # connverting the tuple to list to add  new value
listtuple.append(6)        
tuple1=tuple(listtuple)
print(tuple1)
tuple2= (7,)
tuple1= tuple1+tuple2 #addin a tuple into tuple to add new value in the existing tuple
print(tuple1)
print("on order to remove itmes and other operation we have to convert it to list")
print("---------------------------------------------------------------------------")
v1,v2,v3,*v4= tuple1
print(v1,v2)
print(v4)
print("---------------------------------------------------------------------------")
print("                                                                    loop tuple")
for x in tuple1:
    print(x)
print("looping through the tuple using while loop")
i=0
while i< len(tuple1):
    print(tuple1[i])
    i=i+1
print("the content of a tuple or list can be multiplied with a number")
print(tuple1*2)
print(tuple1+tuple1)
print("---------------------------------------------------------------------------")
print("                                                                     tuple methods")
print(tuple1.count(4))
print(tuple1.index(4))
print("---------------------------------------------------------------------------")
print("                                                                         sets")
set1= {1,2,3,4,5,"a","c",True,False,} # true and 1 are same in sets and same for False and 0
print(set1)
print(len(set1))
set1= set(set1)
print("---------------------------------------------------------------------------")
print("                                                                    Access set items")
print("stet items cannot be accessed using index but we can loop through the set and print the values")
for x in set1:
    print(x)
print("---------------------------------------------------------------------------")
print("                                                                     Add set items")
set1.add(6)
print(set1)
set2={"addomg two sets, to make a new", "containg both set's values"}
set1.update(set2)
print(set1)
set1.update(list5)
print(set1)
print("---------------------------------------------------------------------------")
print("                                                                   Remove set items")
set1.discard(False)  # remove method can also be used to remove an item . Popitem method removes any random item
print(set1)
print("---------------------------------------------------------------------------")
print("                                                                      loop sets")
for x in set1:
    print(x)
print("---------------------------------------------------------------------------")
print("                                                                     Join sets")
set1.union(set2)
set3={1,2,3,4,5}
set4= {"A","B","C","D","E"}
set5=set3.union(set4) # the union does not change the orignal set 
print(set5)
del set5
set5= set3|set4 # the or method does not add different data types
print(set5)
del set5
set5 = set1.union(set3, set4) # adding multiple sets to make new set with all the values
print(set5)
del set5
set5 = set3.union(list5) # union and update methods allow you to join different datatypes to sets
print(set5)
del set5
set5= set3.intersection(set4) # there are no common values in set3 and set4 so the result will be empty set
print(set5)
del set5
set3.intersection_update(set4) # this method will allow you to update the esisting set
print(set3)
del set3
set3 = {1,2,3,4,5}
set5= set3.symmetric_difference(set4) #one's values are not present in other's so the result will contain all the values
print(set5)
del set5
set5= set3^set4
print(set5)
del set5
print("---------------------------------------------------------------------------")
print("                                                                    list methods")
print(set3.isdisjoint(set4)) # returns true if there are no common items between sets
print(set3.issubset(set1)) #returns true if all the items of first set are present in the other
print(set1.issuperset(set3))# returns true if all the items of second set are present
print("---------------------------------------------------------------------------")
print("                                                                    Dictionaries")
dic1= {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
print(dic1["a"]) 
dic2= dict(d= 4,e=5,f=6) 
print(dic2)
print("---------------------------------------------------------------------------")
print("                                                                  Access dict items")
print(dic1["b"])
dicd=dic2.get("d")
print(dicd)
dic1keys= dic1.keys()
print(dic1keys)
dic1values=dic1.values()
print(dic1values)
print(dic1.items())

if "a" in dic1: # checking if a key exists
    print("yes a is present")
print("---------------------------------------------------------------------------")
print("                                                                    change items")
dic1["a"]= 4
print(dic1)
dic1.update({"a":1})
print(dic1)
print("---------------------------------------------------------------------------")
print("                                                                add dictionary items")
print(dic2)
dic2["g"]= 7
print(dic2)
dic2.update({"h":8})
print(dic2)
print("---------------------------------------------------------------------------")
print("                                                                    Remove items")
dic2.pop("h",)
print(dic2)
dic2.popitem()
print(dic2)
del dic2["f"]
print(dic2)
print("---------------------------------------------------------------------------")
print("                                                                 loop dictionaries")
for x in dic1:
    print(x)
for x in dic1:
    print(dic1[x])
for x in dic1.keys():
    print(x)
for x in dic1.values():
    print(x)
for x in dic1.items():
    print(x)
print("--------------------------------------------------------------------------")
print("                                                                  copy dictionaries")
dic3 = dic1.copy()
print(dic3)
dic4= dict(dic2)
print(dic4)
print("--------------------------------------------------------------------------")
print("                                                                 Nested dictionaries")
nestdic1= {
   "veg": {
        "fruit ": "mango",
        "vegetable": "carrot",
        "nut": "almond"
    },
   "non veg" :{
        "animal": "cow",
        "bird"  : "sparrow",
        "reptile": "Snake"
}
}
print(nestdic1)
nestdic2= {
    "child1":dic1,
    "child2":dic2,
    "child3":dic3
}
print(nestdic2)

print("Access items in nested dictionaries")
print(nestdic2["child1"]["a"])
print(" ")
print(nestdic1["non veg"]["animal"])
print("loop nest dictionary")

for x,y in nestdic1.items():
    print(x)
    for z in y:
        print(z +':',y[z])
print("--------------------------------------------------------------------------")
print("                                                                 dictionary methods")
print("from keys method make dictionary from the given specified keys given in the form of tuple")
keys= ("key1","key2","key3")
keyvalue= "fromkeys"
dic5= dict.fromkeys(keys,keyvalue)
print(dic5)
print("setdefault method gives the value of the key only if the key exists otherwise it gives the default value which is none if not specified")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                               inheritance")
class teacher:
  def __init__(self,name,age):
    self.name = name
    self.age= age
  def prnt(self):
    print(self.name,self.age)
t=teacher('zubair',24)
t.prnt()

class student(teacher):
  def __init__(self,name,age,sname,sage):
    super().__init__(name,age)
    self.sname= sname
    self.sage =sage
  def prt(self):
    print(f"the teacher name is {self.name} and is {self.age} years old.the student's name is {self.sname}and is {self.sage}years old ")
s=student("talha",25,"zubair",24)
s.prt()
print("---------------------------------------------------------------------------------------------")
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
file= open("demofile","w")
file.write("this is a test file")
file.close()
file=open("demofile","r")
print(file.read())
file.close()
print("78450610  5319")




