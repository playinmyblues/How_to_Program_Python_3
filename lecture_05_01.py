# This is work from lecture 5 in the course.
# Here is an infinite loop - we usually want to avoid infinite loops
value = -1
while value <= 0:
    # value = 0     # commented out so it does not normally run
    value = 1
    print("value = ", value)

# Here is an example of a while loop - leading up to while loops
num_people = int(input("How many people are there? "))
i = 0
total_age = 0
while (i < num_people):
    age = float(input("Enter the age of person " + str(i+1) + ": "))
    total_age += age
    i += 1
average_age = total_age/num_people
print("The average age was", average_age)

# In a while loop, of the conditional statement has a value that allows the look to stop once
# that value is reached. The way the program progresses is usually in a way that the circumstances
# that meet the condition are indefinite. They do not have to be indefinite, as we can see above.
# When the conditions are very straightforward, a while loop is not really needed and we can use
# a for loop which is seen as having more deifnite conditions under which is it run.

# Here is a simple for loop example
for i in range(4):
    print("i: ", i)

# Here is the same loop for the average age example given above
i = 0
total_age = 0
num_people = int(input("How many people are there? "))
for i in range(num_people):
    age = float(input("Enter the age of person " + str(i + 1) + ": "))
    total_age += age
average_age = total_age/num_people
print("The average age of the", num_people, "people is: ", average_age)

# Here is another example of a for loop with different values in the range area of the loop that
# make the loop run in a particular way, in reverse
# 5 is the starting value, and it runs from 5 down to 1 by steps of -1. You could have different
# values instead of -1. NOTE that it stops printing the values before it gets to 1 in this case
for i in range(5, 1, -1):
    print("i: ", i)

# Here is the same thing with a while loop
i = 5
while i > 1:
    print("i: ", i)
    i -= 1