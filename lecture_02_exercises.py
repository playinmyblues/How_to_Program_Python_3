# This program writes out the code in the exercises as a check against the person's mental
# calculations.

#1
a = 10
b = 15
a += b
print(a) # should be 25

#2
a = 10
b = 15
a = b
b = 1
print(a) # should be 15

#3
a = 10
b = 15
a = a*a+b
print(a) # should be 115

#4
a = 10
b = 15
a *= a+b
print(a)

#5
a = 10
b = float(a)
print(b)

#6
a = "10"
b = int(a)
print(b)

#7
a = "Welcome"
b = "Home"
print(a,b)

#8
a = "Welcome"
b = "Home"
print(a+b)

#9
a = "10"
b = "15"
c = a+b
d = int(c)
print(d)

#10 - Set the price of bread to be 2.00
bread_price = 2.00

#11 - Given a price for a loaf of bread, “bread_price,” and a price for a block of
# cheese, “cheese_price,” calculate the cost to buy 2 loaves of bread and 3
# blocks of cheese.
cheese_price = 3.00
total = bread_price*2 + cheese_price*3
print("2 loaves of bread and 3 blocks of cheese costs $", total)

#12 - get a user's age
print()
users_age = input("What is your age in years? ")
print("You entered:", users_age)

#13 - Write a program to form the name of a knight by asking the user for the
# knight’s name and a personality characteristic. The final name should be
# printed as “Sir <name> the <characteristic>.” For example, if the user enters
# “Robin” and “Brave,” you would print “Sir Robin the Brave.”
knights_name = input("What is the knight's name? ")
characteristic = input("Use one word to describe this knight: ")
print("The knight's moniker is:", knights_name, "the", characteristic)