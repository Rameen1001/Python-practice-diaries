str1="a s d f g h j kl l"
str2="l k j f g h d s a"
str1=str1.replace(" ","")
str2=str2.replace(" ","")
str1=sorted(str1)
str2=sorted(str2)
if str1==str2:
    print("strings are anagram")
else:
    print("strings are not anagram")