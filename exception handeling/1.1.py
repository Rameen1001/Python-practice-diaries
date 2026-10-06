class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return len(self.title)
obj=book("my_book","sadia")
obj1=book("your_book","rameen")
print(obj)
print(obj1)
print(len(obj))
print(len(obj1))