# This version of the program is provided by the course with the idea that it is improving a
# couple of areas of the program. It asks the user's name, the item that the user wants to save
# for, and it adds a couple of relevant messages to communicate information to the user such as
# the number of payments needed. All the other features that were added in previous versions are
# still there.

# Get info from user - this is what is presented, not how I might write my own version
print("I'll help you determine how long you need to save.")
name = input("What is your name? ")
item = input("What is it you are saving up for? ")
# Below is the original line of code provided by the lecture. It provides an error message saying
# that the input() command only expects 1 argument, not 5.
# balance = float(input("OK", name, ". Please enter the cost of the", item, ": "))
# To deal with this, I will make a variable consisting of concatenated strings and use that
# variable in the input() command
name_n_cost_question = "OK " + name + ". Please enter the cost of the " + item + ": "
balance = float(input(name_n_cost_question))
if (balance < 0):
    print("Looks like you have already saved enough.")
    balance = 0
    payment = 1
else:
    payment = float(input("Enter how much you will save each period: "))
    if(payment <= 0):
        payment = float(input("Savings much be positive. Please enter a positive value: "))
# Calculate number of payments that will be needed
num_remaining_payments = balance/payment
# Present information to user
print(name + ", you must make", num_remaining_payments, "more payments, and then you will have your", item + "!")

# Even with typing in mostly what was provided by the lecture, I still had to troubleshoot some
# bugs that involved formatting and even spelling. And then there was the input() problem where
# Python did not like more than 1 argument which was not the case in the lecture.
# TIME: 25:25