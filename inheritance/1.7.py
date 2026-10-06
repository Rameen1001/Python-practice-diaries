class account:
    def __init__(self,username):
        self.username=username
class business_account(account):
    def __init__(self,username,email):
          super().__init__(username)
          self.email=email
    def is_official_partner(self,domain):
         self.email=self.email.split("@")
         print(self.email[-1])
         if self.email[-1]==domain:
              print("email ends with target domain")
         else:
              print("does not end with target domain")
obj=business_account("rameen","rameenf404@gmail.com")
obj.is_official_partner("gmail.com")
                  