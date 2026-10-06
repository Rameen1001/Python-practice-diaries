class animal:
    def __init__(self,name):
        self.name=name
class dog(animal):
    def __init__(self,name,sound="woof"):
        super().__init__(name)
        self.sound=sound
    def speak(self,times):
        if(times>0):
            for i in range (times):
               print(f"{self.sound}", end=" ")
        else:
            print("nothing")
obj=dog("tom")
obj.speak(5)
        