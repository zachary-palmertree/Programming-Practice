# This is a basic Python program that greets the user.

# 1. Get the user's name.
name = input("What is your name?")

# 2. Greet the user.
print("Hello, " + name + "!")

# 3. Perform a simple calculation.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
sum = number1 + number2

# 4. Display the result.
print("The sum of", number1, "and", number2, "is:", sum)

# 5. A simple conditional statement.
if sum > 10:
    print("That's a big sum!")
else:
    print("That's a small sum.")

# 6. A simple loop to print numbers.
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)