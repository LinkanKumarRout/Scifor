# creating a function
def funcName(a,b): # function definition
  print(a+b)

funcName(10, 20) # function call

def display(a,b,c):
  x = a + b + c
  print(x)

# display(10, 20, 30, 40) # this give error
# display(10,20) # error
display(10,24,45)
# here a, b and c are called as formal/positional arguments
# here 10, 24 and 45 are called as actual arguments
# if we provide different no. of arguments during function call it will give us error

def display(m, n=10): # here n is called default argument and m is called non-default argument
  for i in range(n):
    print(m)

display('python') # no need to provide n value bcz it is default
display("hi",n=3) # n is called keyword argument

name = "linkan" # global variable
def display():
  a = 10 # local variable
  b = 20 # local variable
  print(a + b)
  print(f"Hello {name}") # this will not give error bcz name is a global variable

display()
# print(b) # this gives error bcz b is local variable

a = 10
print(a) # 10
def display():
  global a # refers to global value of a
  a += 5
  print(a)
display()
print(a)