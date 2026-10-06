class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def cal_total(self,tax_rate):
        return self.price+self.price*tax_rate/100
class physical_product(product):
    def __init__(self,name,price,shipping_weight):
        super().__init__(name,price)
        self.shipping_weight=shipping_weight
    def cal_total(self,tax_rate):
        return self.price+self.price*tax_rate/100+5
class digital_product(product):
    def __init__(self,name,price,file_size):
        super().__init__(name,price)
        self.file_size=file_size
    def cal_total(self,tax_rate):
        return self.price
p1=physical_product("beater",800,2)
print(p1.cal_total(10))
p2=digital_product("word",1000,"10mb")
print(p2.cal_total(20))
