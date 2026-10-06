class employee:
    def __init__(self,salary):
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,new_salary):
        if new_salary<0:
            print("enter positive value")
        else:
           self._salary=new_salary
obj=employee(12000)
print(obj.salary)
obj.salary=-1300
print(obj.salary)
