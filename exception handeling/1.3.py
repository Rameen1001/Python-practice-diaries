class invalid_num(Exception):
    def __init__(self,message="invalid number"):
        self.message=message
        super().__init__(message)
def verify_number(n):
    if n<0:
        raise invalid_num()
    return "positive"
try:
    print(verify_number(-4))
except invalid_num as e:
    print(f"error{e}")
