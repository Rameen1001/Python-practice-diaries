class item:
    def __init__(self,title,catalog_id):
        self.title=title
        self.catalog_id=catalog_id
class book(item):
    def __init__(self,title,catalog_id,author,genere):
        super().__init__(title,catalog_id)
        self.author=author
        self.genere=genere
    def belongs_to_genere(self,search_genere):
        for i in self.genere:
            if search_genere.upper()==i.upper():
                return True
       # else:
        return False
genere=["abc","def","ghi"]
book1=book("jannat",1,"umaira",genere)
print(book1.belongs_to_genere("gHi"))

       