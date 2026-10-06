class member:
    def __init__(self,name):
        self.name=name
class student(member):
    def __init__(self,grades):
        self.grades=grades
    def has_passed_all(self):
        for i in self.grades:
            if i<50:
                return False
        return True
grades=[50,50,60]
grade=[30,50,63]
obj=student(grades)
obj2=student(grade)
print(obj.has_passed_all())
print(obj2.has_passed_all())