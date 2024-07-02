#1. Read a text file using python
#1. read a text file using python
with open('aboutPython.txt', 'w') as file:
  file.write("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics devloped by Guido van rossum in 1989.\nIt's high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.\nPython's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.\nPython supports modules and packages, which encourages program modularity and code reuse.\nThe Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.")

with open('aboutPython.txt', 'r') as file:
  data = file.read()
  print(data)

#2.
'''
Himanshi has a text file and she wants to check whether that file contains any numerical value.
So to help Himanshi write a python program that can check whether the text file includes any numerical value or not.
As text files contain so many lines, so print the line number that has numerical values
'''
with open('aboutPython.txt', 'r') as file:
  line_number = 0
  for line in file.readlines():
    line_number += 1
    flag = False
    for ch in line:
      if ch.isdigit():
        flag = True
        break
    if flag:
      print(f"Line {line_number} : {line}")

#3. Calculate all BMI records and save it in a file
import datetime

def calculate_bmi(height, weight):
  bmi = weight / ((height/100)**2)
  return bmi

def record_bmi(height, weight, bmi):
  time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  with open('bmi.txt', 'a') as file:
    file.write(f"Height : {height/100} meter, Weight : {weight} kg, BMI : {bmi:.2f}, Time : {time}\n")

height = int(input("Enter your Height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = calculate_bmi(height, weight)
print(f"Your BMI is: {bmi:.2f}")

record_bmi(height, weight, bmi)
print("BMI recorded successfully....")

view_records = input("Do you want to view all BMI records (yes/no) ? ").lower()
if view_records == 'yes':
  with open('bmi.txt', 'r') as file:
    data = file.read()
    print(data)
else:
  print("Bye...")

#4. Add line numbersfile
# creating a file
with open('hugeFile.txt', 'w') as file:
  file.write('''Python is a high-level, interpreted programming language known for its simplicity and readability.
  It was created by Guido van Rossum and first released in 1991.
  Python emphasizes code readability with its clear and concise syntax, making it accessible to both beginners and experienced developers alike.
  Its dynamic typing and automatic memory management contribute to rapid development cycles, enabling programmers to focus on solving problems rather than managing language complexities.
  Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
  Its extensive standard library provides built-in modules and functions for various tasks, ranging from file I/O to networking, making it suitable for a wide range of applications, such as web development, data analysis, machine learning, artificial intelligence, and scientific computing.
  Python's versatility and flexibility have led to its widespread adoption in industries and academia.
  It powers popular frameworks and libraries like Django, Flask, NumPy, pandas, TensorFlow, and scikit-learn, facilitating the development of robust and scalable applications.
  Python's community-driven development model fosters collaboration and innovation, with a vibrant ecosystem of developers contributing to its growth.
  Its open-source nature encourages transparency and accessibility, allowing developers to inspect, modify, and distribute the source code freely.
  Python's popularity continues to grow, driven by its ease of learning, extensive documentation, and active community support.
  Its cross-platform compatibility enables developers to write code once and run it on multiple platforms without modification, further enhancing its appeal.
  Overall, Python's simplicity, versatility, and community support make it a powerful tool for solving complex problems and driving innovation in the modern software development landscape.\n''')

# Reading a file and adding line number at the beginning of each line
with open('hugeFile.txt', 'r') as file:
  line_number = 0
  lines = file.readlines()
  allLine = []
  for line in lines:
    line_number += 1
    line = str(line_number) + "." + line
    allLine.append(line)
  with open('hugeFile.txt', 'w') as fi:
    fi.write(''.join(allLine))

# Reading the modified file
with open('hugeFile.txt', 'r') as file:
  data = file.read()
  print(data)

#5. Replace a misspelled word in a file
# creating the file
with open('file4.txt', 'w') as file:
  file.write('''Python is a popular langauge used for programming due to its simplicity and versatility.
  It is widely used in web development, data analysis, and machine learning.
  With its clear syntax and extensive libraries, Python makes it easy to develop complex applications.
  Many programmers prefer Python over other langauge because of its readability and ease of use.
  Learning Python langauge can open up many opportunities in the field of software development.
  As a dynamically typed langauge , Python allows developers to write code more quickly and efficiently.
  Overall, Python is a powerful langauge that continues to grow in popularity.''')

incorrect_word = "langauge"
correct_word = "language"

print("Before.....\n")
with open('file4.txt') as file:
  print(file.read())
# read and change mis-spelled word
with open('file4.txt') as file:
  data = file.read()
  data = data.replace(incorrect_word, correct_word)
  with open('file4.txt', 'w') as fi:
    fi.write(data)

print("\nAfter.....\n")
with open('file4.txt') as file:
  print(file.read())

#6. add a line break after a digit
# reading data from file
with open('hugeFile.txt', 'r') as infile:
  org_data = infile.read()
  print("Before.....\n")
  print(org_data)

  mod_data = ''
  for char in org_data:
    if char.isdigit():
      mod_data += char
    elif char == '.':
      mod_data += '.\n'
    else:
      mod_data += char
  with open('hugeFile.txt', 'w') as outfile:
    outfile.write(mod_data)
print("\nAfter.....\n")
with open('hugeFile.txt') as fi:
  print(fi.read())

#7. Remove duplicate words in a file
with open('file4.txt') as file:
  org_data = file.read()
  print("Before.....\n")
  print(org_data)
  mod_data = []
  for word in org_data.split():
    if word not in mod_data:
      mod_data.append(word)
  with open('file4.txt', 'w') as fi:
    fi.write(' '.join(mod_data))

print("\nAfter.....\n")
with open('file4.txt') as fi:
  print(fi.read())
