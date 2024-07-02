# Write data in a file
file = open('info.txt', 'w') # open a file in write mode
file.write("Hello Everyone !\nThis is the first file.") # write something in the file
file.close() # close the file

# Read Data from a file
file = open('info.txt', 'r')
data = file.read() # read everything written in the file
print(data)

# Read single line
file = open('info.txt', 'r')
line = file.readline() # this only reads the first line
print(line)

#Read all line in a file
file = open('info.txt', 'r')
data = file.readlines() # read all line in a list
print(data)

# Apped something to an existing file
file = open('info.txt', 'a')
file.write("\nThis is second line")
file.close()
file = open('info.txt', 'r')
data = file.read()
print(data)

# Write something to a file without closing it
with open('info.txt', 'a') as file:
  file.write("/nThis is third line")
  print("File saved successfully")

# OS module and how to delete a file
import os
os.remove('info.txt')
print('file got deleted successfully')
file = open('info.txt', 'r') # this will give FileNotfoundError
data = file.read()
print(data)
