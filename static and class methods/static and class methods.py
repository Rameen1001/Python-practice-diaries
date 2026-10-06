class mathutils:
    @staticmethod
    def add (a,b):
        return a+b
    @classmethod
    def description(cls):
        print("this is a utility class for math operatrions")
print(mathutils.add(3,5))
mathutils.description()