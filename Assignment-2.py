#1. Calculate no. of chocolates left
noOfChocolate = 327
noOfKids = 78
remaining = noOfChocolate % noOfKids
print(f"Remaining chocolate after giving chocolate to students is {remaining}")

#2. Contest Participation in a Resturant
print("It's our 25th Anniversary. Please provide your details for participating in the contest.")
name = input('Enter your name: ')
age = input('Enter your age: ')
mobile = input('Enter your Mobile no.: ')
emailId = input('Enter your Mail ID: ')
print(f"Hi, {name},!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.")
print(f"Once the lucky draw results are announced you will receive a message on your mobile number :{mobile}")
print(f"An detailed description of your gift on your email Id :{emailId}. Thank you for being a valued customer, {name}!! Dominos")

#3. Calculate no. of teams
group = 4
totalStudents = 60
teams = totalStudents // group
print(f"Total no. of teams will be {teams}")

#4. Convert Fahrenheit to Celcius
tempInFahrenheit = 45
tempInCelsius = (tempInFahrenheit - 32) * 5/9
print(f"Temperature in Celsius is {round(tempInCelsius,2)}")