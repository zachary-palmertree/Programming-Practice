import time

print('hello world!')

# I need to understand the difference between a method, function, and class.
# I know a method is attributed to an object, and is of the form
# object.method(parameters)

# Function to print out argument slowly
def print_slowly(input):
    print(input)

# Method is a function associated with a specific object or class
class Person:
    def greet(self, name):
        return f"Hello, {name}!"

person = Person()
message = person.greet("Alice")
print(message)

# Use a class when you need 1) structured data with behavior
# 2) complex logic 3) custom data types
# 4) encapsulation
class test:
    # class definition
    name = ''
    age = 0
    ID = 0

# Use dictionary for 1) simple data storage 2) no complex behavior
# 3) dynamic data 4) JSON-Like Data

# This is a list of dictionaries
people = [] # dictionary to contain each person's dictionary
zach = {'name' : 'Zach', 'age' : 25, 'ID' : 1}
bill = {'name' : 'Bill', 'age' : 55, 'ID' : 2}


# Now we add the people to the primary people dictonary
people.append(zach)
people.append(bill)
print(people[0]['name'])

# Another way we can handle multiple dictionaries is to have
# a dictionary of dictionaries
people = {}
people['zach'] = {'ID':'001','name':'Zach', 'age': 25}
# Access a nested element of the dictionary
print(people['zach']['ID'])