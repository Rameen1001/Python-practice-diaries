class vector_3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __mul__(self,other):
        return vector_3D(self.x*other,self.y*other,self.z*other)
    def __repr__(self):
        return f"vector_3D({self.x},{self.y},{self.z})"
v=vector_3D(2,3,5)
print (v*3)