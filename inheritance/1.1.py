class clothing:
    def __init__(self,color,size):
        self.color=color
        self.size=size
class shirt(clothing):
    text_print="clean"
    def is_clean_slogan(self):
        if len(self.text_print)<=15:
            return "true"
        else:
            return "false"
obj=shirt("green", "medium")
print(obj.is_clean_slogan())
        
