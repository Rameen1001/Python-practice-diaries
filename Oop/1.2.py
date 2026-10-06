class circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
       area=3.14*self.radius*self.radius
       return area
a=circle(5)
obj=circle(3)
print(obj.get_area())
b=a.get_area()
print(b)

    