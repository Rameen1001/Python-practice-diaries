def safe_divide(a,b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a/b
print(safe_divide(25,0))