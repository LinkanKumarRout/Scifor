'''
import random
print(random.random()) # returns a random float number between 0 & 1
print(random.randint(1,10)) # returns a random number between given range

lst = ['apple', 'banana', 'cherry', 'date']
print(random.choice(lst)) # returns a random element from non-empty sequence
random.shuffle(lst) # shuffle elements in a sequence
print(lst)

lst = list(range(1,100))
print(random.sample(lst, 5)) # returns a random list of k elements from a sequence
# in the above case it's returning 5 random elements between 1 to 100

print(random.uniform(1,3)) # gives a random float number between 1 and 3

print(random.randrange(0, 101, 5))  # Random number between 0 and 100 with a step of 5

random_bits = random.getrandbits(16)  # Generates a random integer with 16 random bits
print(random_bits)

population = ['red', 'green', 'blue']
weights = [0.3, 0.5, 0.2]
choices = random.choices(population, weights, k=4)  # Selects 4 elements from the population with specified probabilities
print(choices)
'''
