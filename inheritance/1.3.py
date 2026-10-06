class user:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
class spy(user):
    def generate_code_name(self):
        code=self.fname[:2].upper()+self.lname[-1].upper()
        return code
name1=spy("rameen","fatima")
name2=spy("filzah","aslam")
print(name1.generate_code_name())
print(name2.generate_code_name())