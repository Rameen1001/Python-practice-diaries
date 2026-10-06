class vehicle:
    def __init__(self,for_make,model):
        self.for_make=for_make
        self.model=model
class car(vehicle):
    def __init__(self,for_make,model,mpg_history):
        super().__init__(for_make,model)
        self.mpg_history=mpg_history
def find_gas_guzzlers(car_list):
    for car in car_list:
        total=0
        count=0
        for i in car.mpg_history:
            total+=i
            count+=1
        avg=total/count
        if avg<25:
            print(f"{car.for_make} {car.model} is a gass guzzler")
        else:
            print(f"{car.for_make} {car.model} is not a gas guzzler")
car1=car("corolla",2025,[3,60,40,20])
car2=car("honda",2026,[2,3,4,5])
car_list=[car1,car2]
find_gas_guzzlers(car_list)


        

    
