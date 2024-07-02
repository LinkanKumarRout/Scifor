#1. Print a name as well as his age in a single line

print('Arvind')
print('Linkan', 25)

#2. Print different shapes just using print statement

print("Different shapes using symbols like |, /, \, -")
print(".....Rectangle.....\n")

print("|", "-" * 10, "|")
print("|", " " * 10, "|")
print("|", " " * 10, "|")
print("|", " " * 10, "|")
print("|", "-" * 10, "|")
print()

print(".....Square.....\n")

print("----------")
print("|        |")
print("|        |")
print("|        |")
print("----------")

print()
print(".....Triangle.....\n")

print("     /\ ")
print("    /  \ ")
print("   /    \ ")
print("  /      \ ")
print(" /--------\ ")

print()

print(".....Diamond.....\n")

print("   /\ ")
print("  /--\ ")
print(" /----\ ")
print("/------\ ")
print("\------/")
print(" \----/")
print("  \--/")
print("   \/")
#3. Print your friend names just using a print statement

print("Ram\nSagar\nSurya\nAjay\nNirmal")

#4. Essay generator

print("Welcome to the essay generator!")
print("Please provide the following details:")

name = input("Enter your Name: ")
age = input("Enter your Age: ")
address = input("Enter your Address: ")
hobbies = input("Hobbies: ")
achievements = input("Enter Achievements: ")
goals = input("Enter your Goals: ")

essay = f"\nEssay on {name}:\n"
essay += f"My name is {name}. I am {age} years old and I live at {address}.\n"
essay += f"I have several hobbies, some of which include {hobbies}.\n"
essay += f"Among my achievements, I am proud of {achievements}.\n"
essay += f"My goals in life include {goals}.\n"
essay += "In conclusion, I am a motivated individual with a passion for learning and growth."

print("\nGenerated Essay:\n")
print(essay)

#5. A simple chatbot using python

# A simple chatbot using python
name = input('Hi, i am a chatbot. What is your name ? ' )
grade = input(f"Oh, {name} in which grade you are right now? " )
ques = input(f"{name} you are in {grade}th grade. Can i ask you a question ?(yes/No) ").lower()
if ques == 'yes':
  ans = int(input("Tell me 1024+98=?"))
  if ans == 1122:
    print("Good! Your answer is correct. Bye")
elif ques == 'no':
  print("OK. Bye !")
else:
  print("Please answer in yes/no only")

#6. calculate price of no. of books

noOfBooks = int(input('Enter the number of books to buy: '))
print(f"You have to pay {noOfBooks*2}$.")

#7. A simple calculator

num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
print(f"Addition = {num1 + num2}")
print(f"Subtraction = {num1 - num2}")
print(f"Multiplication = {num1 * num2}")
print(f"Division = {num1 / num2}")

#8. Age calculator

current = 2024
dob = int(input('Enter your birth year: '))
print(f"Your age is {current - dob}")