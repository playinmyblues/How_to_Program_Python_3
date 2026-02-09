# This is the 3rd file covering material for chapter 7. Page 76 - Tuples.
# Tuple - a list whose values can never change and unlike a list, often contains different types
# of data.

# Below is a quick example. The first line defines the tuple. The second line breaks the tuple down
# and assigns the values to the variables that are separated by commas.
car_tuple = "Buick", "Century", 23498
make, model, mileage = car_tuple
print("Make:", make)
print("Model:", model)
print("mileage:", mileage)
# You can also use slicing with tuples as you can with a list
print("car_tuple[1:] gives you:", car_tuple[1:])
print(car_tuple)

# Exercises from chapter 7, starting on Page 77
# Ex 1, guess the result, outputs: 4:
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("my_list[1]:", my_list[1])

# Ex 2, outputs: [6, 8, 10] - originally, I did not include the square brackets
print("my_list[2:5]:", my_list[2:5])

# Ex 3, outputs: [2, 4, 6]
print("my_list[:3]:", my_list[:3])

# Ex 4, outputs: 8th item to the end, [16, 18, 20]
print("my_list[8:]:", my_list[8:])
# THIS ACTUALLY OUTPUTS STARTING AT THE ITEM WITH Index #8, until the end, Index 8 has 18

# Ex 5, output: the whole list, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("my_list[:]:", my_list[:])

# Ex 6, outputs: the last element of the list, 20
print("my_list[-1]:", my_list[-1])

# Ex 7, outputs: the last three elements of the list, in square brackets, [16, 18, 20]
print("my_list[-3:]:", my_list[-3:]) # watch for user errors - I left out the colon, result: 16

# Ex 8, outputs: the whole list in square brackets, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("my_list:", my_list)

# Ex 9, outputs: each element of the list, number only, no brackets, each on its own line
for item in my_list:
    print(item)
# NOTE that they use i instead of item in the for loop. For me, I think of i as the index value,
# not the item in the index location. i would work as well though as Python does not think.

# Ex 10, outputs: the 4th item (index #3) is assigned the value of 100
my_list[3] = 100
print("my_list:", my_list)

# Ex 11, outputs: a list with 10 items, each item is 0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in my_list:
    i = 0
print("my_list:", my_list)

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for i in mylist:
    i = 0
print (mylist)
# The above code, both versions, do nothing to the list. If I start using the index with the list
# name, it should change the items of the list. See below.
index = 0
for item in my_list:
    my_list[index] = 0
    index += 1
print("my_list:", my_list)

# Ex 12, outputs: appends 100 to the end of the list: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 100]]
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_list.append(100)
print("my_list.append(100):", my_list)

# Ex 13, outputs: I guess that it deletes items at indices 1 to 5, inclusive:
# [2, 14, 16, 18, 20]
mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_list[1:5] = []
print("mylist[1:5] = [] produces:", my_list)
# It produces [2, 12, 14, 16, 18, 20], remember, with slicing, the second number is the one
# after the one you want to stop at
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("my_list:", my_list)
print("my_list[1:5]:", my_list[1:5])

# Ex 14, the code below replaces items at indices 2 to 7, inclusive, with items 100 and 200
# It should look like [2, 4, 100, 200, 18, 20]
my_list[2:8] = [100, 200]
print("my_list[2:8] results in:", my_list)

# Ex 15, the code below results in no change to my_list
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_list[2:2] = [100]
print("my_list[2:2] = [100] results in:", my_list)
# It was a bit of a guess but the results are not exactly consistent with the information given
# about slicing in chapter 7. But the information was provided in the form of the exercise.

# Ex 16, Given a list of integers named “ages,” form a new list named “minor_ages”
# consisting of all those ages from the “ages” list that are less than 18.
ages = [19, 23, 15, 18, 16, 32, 44, 14, 28]
minor_ages = []
less_than_age = 18
for item in ages:
    if (item < less_than_age):
        minor_ages.append(item)
print("minor_ages:", minor_ages)

# Ex 17, Create a list containing two lists: one with names of 3 people and one with
# ages of 3 people (you can choose the names/ages).
#names_and_ages = []
names = []
ages = []
index = 0
while index < 3:
    names.append(input("Please enter the name for person #" + str(index + 1) + ": "))
    age_input_string = "Enter " + names[index] + "'s age: "
    ages.append(int(input(age_input_string)))
    index += 1
names_and_ages = [names, ages]
print("names_and_ages: ", names_and_ages)
print("And again, but with a for loop:")
names_2 = []
ages_2 = []
for index in range(3):
    names_2.append(input("Please enter the name for person #" + str(index + 1) + ": "))
    ages_2.append(int(input("Enter " + names_2[index] + "'s age: ")))
names_and_ages_2 = [names_2, ages_2]
print("names_and_ages_2: ", names_and_ages_2)