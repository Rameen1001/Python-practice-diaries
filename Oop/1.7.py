class animal:
    def sound(self):
        print("some sound")
class dog(animal):
    def sound(self):
        print("woof")
obj=dog()
obj.sound()
obj2=animal()
obj2.sound()