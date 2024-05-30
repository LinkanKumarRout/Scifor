#1. Calculate Probability
noOfFav = eval(input('Enter total number of Favourable Outcome: '))
totalOutcome = eval(input('Enter total number of Outcome: '))
print("Probability is",round(noOfFav/totalOutcome, 2))

#2. RTO Registration
print("Register Yourself for Driving License...")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
  print(f"{name}, you are greater than 18 years old")
else:
  print("You are not 18 years old, Please come back later.")

#3. Simple chatbot
username = input("Hi there! What's your name? ")
print(f"Hi, my name is Scarlet, your chatbot. A Very Good Day To You, {username}!!")
user_feeling = input("How are you feeling today? ")
if "good" in user_feeling.lower() and "not good" not in user_feeling.lower():
    print("It's really a productive day to do something innovative and you are close to it.")
elif "bad" in user_feeling.lower() or "not good" in user_feeling.lower():
    print("I'm sorry to hear that. Remember, every cloud has a silver lining. Stay positive!")
else:
    print(f"Don't worry!! you got this {username}!!. buckle up and cheer yourself up. Good days are on their way. There is no beautiful rainbow without a heav.")

#4. Create a ATM Machine
print("Welcome Sir/Mam to the ATM!!")
bank_balance = 50000
while True:
    print("\nATM Machine Options:")
    print("1) Withdraw")
    print("2) Deposit Cash")
    print("3) Balance Enquiry")
    print("4) Fast Cash")
    print("5) Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter withdrawal amount: "))
        if amount % 100 != 0:
          print("Error: Withdrawal amount must be in multiples of 100.")
        elif amount > bank_balance:
          print("Error: Insufficient funds.")
        else:
          bank_balance -= amount
          print(f"Withdrawn {amount} successfully. Current balance: {bank_balance}")
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        bank_balance += amount
        print(f"Deposited {amount} successfully. Current balance: {bank_balance}")
    elif choice == 3:
        print(f"Your account balance is: {bank_balance}")
    elif choice == 4:
        print("Available Fast Cash Options:")
        print("1) 5000")
        print("2) 10000")
        print("3) 15000")
        print("4) 20000")
        print("5) 25000")
        print("6) 30000")
        print("7) 40000")
        print("8) 45000")
        print("9) 50000")
        option = int(input("Select an option: "))
        fastcash = options[option - 1]
        options = [5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000]
        if fastcash in options:
          if fastcash > bank_balance:
            print("Error: Insufficient funds.")
          else:
            bank_balance -= fastcash
            print(f"Withdrawn {fastcash} successfully. Current balance: {bank_balance}")
        else:
          print("Error: Invalid option for fast cash.")
    elif choice == 5:
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please enter a valid option.")

#5. Interest Calculator
principal_yash = 10000
principal_vishal = 10000

rate_of_interest = 6 / 100
time_period = 30

simple_interest_yash = principal_yash * rate_of_interest * time_period
compound_interest_vishal = principal_vishal * ((1 + rate_of_interest) ** time_period - 1)
difference_in_returns = compound_interest_vishal - simple_interest_yash
one_year_difference = (compound_interest_vishal - simple_interest_yash) / time_period

print("Difference in returns after 30 years:", round(difference_in_returns, 2))
print("Difference in returns in one year:", round(one_year_difference, 2))

#6. Calculate Tax to be paid
annual_income = float(input("Enter your annual income: "))

monthly_income = annual_income / 12
tax_per_month = 0.10 * monthly_income
tax_per_year = 12 * tax_per_month

print(f"Tax to be paid based on your annual income is {tax_per_year}")

#7. BMI Calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

height_in_meter = height / 100
bmi = weight / (height_in_meter ** 2)

print(f"Your BMI is {round(bmi, 2)}")
print("You are: ", end = "")
if bmi < 18.5:
  print("Under weight")
elif bmi >= 18.5 and bmi < 25.0:
  print("Normal(Healthy) weight")
else:
  print("Overweight")

#8. A program to check a year is a leap year or not

year = int(input("Enter a year: "))

if year % 400 == 0:
  print(f"{year} is a leap year")
elif year % 100 == 0:
  print(f"{year} is not a leap year")
elif year % 4 == 0:
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")
