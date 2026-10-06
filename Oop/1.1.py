class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello {self.name}")
my_name=person("Rameen",56)
name=person("Filzah",29)
print(my_name.age)
print(name.name)
print(name.age)
my_name.greet()



