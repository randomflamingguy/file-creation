new_file = open('newfile.txt', 'x')
new_file.close()
import os
print("checking if myfile exists or not....")
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("File doesn't exist")
myfile = open('myfile.txt', 'w')
myfile.write("Hi! I am a penguin that is 12 years old")
myfile.close()
os.remove('codingal.txt')
os.rmdir('penguin')