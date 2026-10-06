class potion:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def __add__(self,other):
        return potion(self.name+"-"+other.name,self.power+other.power+10)
    def __str__(self):
        return f"{self.name},{self.power}"
obj=potion("health",20)
obj2=potion("mana",40)
print(obj+obj2)
    