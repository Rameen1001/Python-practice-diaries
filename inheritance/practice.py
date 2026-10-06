
def fun(string):
    new_string=""
    for s in string:
       if s not in new_string:
          new_string=new_string+s
    for i in new_string:
       print(i,string.count(i),end="")

           
fun("aadgfg")