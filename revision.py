import os
import pyjokes

joke = pyjokes.get_joke()
print(joke)
import pyttsx3
engine = pyttsx3.init()



engine.say("I will speak this text")
engine.runAndWait()

# Specify the directory path


directory = "//"

# List all files and folders in the directory
contents = os.listdir(directory)

print("Contents of the directory:")
for item in contents:
    print(item)


