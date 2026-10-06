class member:
    def __init__(self,name,id_code):
        self.name=name
        self.id_code=id_code
class student(member):
    def __init__(self,name,id_code,grades_list):
        super().__init__(name,id_code)
        self.grades_list=grades_list
def audit_students(student_list):
    fun=lambda id_code: id_code[:3]=="STU"
    for student in student_list:
        total=0
        count=0
        if fun(student.id_code):
         for i in student.grades_list:
             total+=i
             count+=1
         avg=total/count
         if avg>=60:
          print(f"{student.name}  pass")
         else:
          print(f"{student.name}  fail")
obj=student("rameen","STU123",[30,40,60])
stu1=student("filzah","STU456",[10,30,20])
audit_students([obj,stu1])