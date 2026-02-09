# This program covers topics from chapter 2. Variables can be both prompts for input as
# well as have values assigned to them from input. There are more ways than these two to
# use variables in programs.

a = input("Enter a value: ")
print(a)
b = input()
print("You entered", b)

# Here is another way to use input and variables
c = "Please enter a value:"
d = input(c)
print("You entered: ", d)

# Let's try this again:
print("3rd Time:")
e = "Enter a value: "
f = input(e)
print("You entered: ", f)

# Example from p23
a = input("Enter value one: ")
b = input("Enter value two: ")
# The line below concatenates the two numbers as the values are entered as strings.
print("The sum is ", a + b)
# Here is the same operation with no string before it in the print statement and the result is
# the same
print(a + b)

# However, we can convert inputs from strings to numbers if they are of the numerical type to our
# eyes.
a = "1"
b = "3.14159"
print(a + b)
c = int(a)
d = float(b)
print(c + d)