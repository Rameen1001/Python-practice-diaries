class vector:
    def __init__(self,l):
        self.x , self.y , self,z = l

    def __len__(self):
        return len(self.l)

v1 = vector([1,2,3])
v2 = vector([4,5,6])
print(len(v1))
print(len(v2))