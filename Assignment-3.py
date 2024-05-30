#1. Check name is palindrome or not
petName = input("Enter a pet name to check: ").lower()
if petName == petName[-1::-1]:
  print("True")
else:
  print("False")

#2. Converting a sentence to secret language
# Converting a sentence to secret language
sentence = input("Enter a sentence to convert it to Secret language: ")
s = []
for i in sentence.split():
  evenCh = ""
  oddCh = ""
  evenCh += i[0::2]
  oddCh += i[1::2]
  word = oddCh + evenCh
  s.append(word)
print("Your secret language is:",' '.join(s))

# Reversing secret word to original sentence is also possible like this.

secret = input('Enter your secret language: ')
original = []
for word in secret.split():
  evenCh = word[-2::-2]
  oddCh = word[-1::-2]
  normal = evenCh + oddCh
  original.append(normal)
print("Original sentence is:",' '.join(original))

#3. Program to check a mobile number is valid or not
mobile = input('Enter a mobile number: ')
if mobile.isdigit():
  if len(mobile) == 10 and mobile[0] in '987':
    print('Valid mobile number')
  else:
    print('Invalid mobile number')
else:
  print('Enter digits only')