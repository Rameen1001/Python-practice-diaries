class temperature:
    def __init__(self,celcius):
        self.celcius=celcius
    def to_fahrenheit(self):
        return self.celcius*1.8+32
obj=temperature(32)
print(obj.to_fahrenheit())
