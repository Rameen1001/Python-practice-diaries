class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class electronic(product):
    def __init__(self,name,price,on_sale):
        super().__init__(name,price)
        self.on_sale=on_sale
def cal_cart_total(product_list):
    total=0
    for item in product_list:
        if isinstance(item,electronic) and item.on_sale:
            item.price=item.price-item.price*20/100
            total+=item.price
        else:
            total+=item.price
    return total
obj=electronic("beater",1500,True)
obj1=electronic("chopper",800,True)
print(cal_cart_total([obj,obj1]))

