class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} says woof")
obj=dog("levis","bjkjj")
obj.bark()
print (obj.name)