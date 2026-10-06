words=["python","rock","ai"]
result=[length for word in words if (length:=len(word))>=4]
print(result)