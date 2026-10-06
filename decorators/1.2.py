import time
def timer(func):
    def wrapper():
        total_time=0
        start=time.time()
        func()
        end=time.time()
        total_time=end-start
        print(total_time)
    return wrapper
@timer
def my_fun():
    sum=0
    for i in range (1000000):
        sum=sum+i
    print(sum)
my_fun()
