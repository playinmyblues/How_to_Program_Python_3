# This program works through the exercises at the end of the chapter 6 in the PDF.
# Ex.1: open a file in the current directory for reading. Call it data.txt.
myfile = open("data.txt", "r")
for line_in_file in myfile:
    print(line_in_file)
myfile.close()

# Ex.2: Open a file named "data.txt" in the directory above the current one for writing.
# It is worth noting here that when I first wrote the code below, I used the word "write" a lot in
# the variable names. The resulting code became a little unruly because it made the intent of the
# code unclear. Everytime I saw "write" I had to wonder if it was a command or a name.
file_used = open("../data.txt", "w")
line = """This line contains a string. Strings are data too.
And again."""
file_used.write(line)
file_used.close()
# It is worth noting that using the """content""" way of specifying a string works well enough.
# However, all of the formatting that occurs in this editor happens in the resutling text file
# created. If I were to add a tab to the second line in the string variable with the triple quotes
# then that tab would also show up on the second line. This is important if you want all of your
# code to look consistent. You might want to choose another way of dealing with those lines of text.

# Ex.3 Given an open "infile," read and print each line in the file.
myfile = open("results.txt", "r")
for line_to_use in myfile:
    print(line_to_use)
myfile.close()
# This works well enough, however, it does not show the commands that can also be used to read a
# single line or the succession of the same command that can be used to read more than one line
# if used repeatedly.
# There might be a better way to code this but I am going to open the file, work on counting the
# number of lines in the file, then use that number to read the lines and print them using a loop
myfile = open("results.txt", "r")
i = 0
line_checked = myfile.readline()
if(line_checked != ""):
    while line_checked != "":
        print(line_checked)   # line gets commented out once code is confirmed to work
        line_checked = myfile.readline()
        i += 1
        # print("i:", i)    # line get commented out once code is confirmed to work
myfile.close()
# Now to run a second loop that runs through the lines to process them. This is not a particularly
# efficient example of a program but it shows that the code counts lines in the file. Then it shows
# that a file can be read again and the lines have something else done with them.
print("i:", i)
j = 0
contentsOfFile = []
myfile = open("results.txt", "r")
print("Just before while loop to create an array of strings")
while j < i:
    line_from_file = myfile.readline()
    print(line_from_file)
    contentsOfFile.append(line_from_file)
    j += 1
print(contentsOfFile)
myfile.close()
# When I first wrote this code, I had a problem with getting the array to work properly. That was
# solved by reading a little more about it online. Then I had the problem of nothing being assigned
# to the array even though the code looked like it should. I knew that the previous loop was still
# reading the file properly but the second loop, even though it had the correct number of cycles
# for the loop, was assigning nothing to the array. Why? I figured that the readline() command was
# stuck at the end of the file. I closed the file, opened it again and the code worked as I
# expected.

# Ex.5: Ask a user for a filename, and then write the numbers 1 to 10, one per line, to that file.
print()
file_name = input("Provide the name of the file: ")
myfile = open(file_name, "w")
for i in range(10):
    myfile.write(str(i + 1) + "\n")
myfile.close()

# Ex.6: Assume that you have a data file named “data.txt” that consists of integers,
# one per line. Find and print the average of those numbers. (Hint: You will
# want to keep a running total of the sum of numbers and how many numbers
# you’ve read in.)
# LET'S CALL THAT FILE "data2.txt" - and it will be created in this program
file_name = "data2.txt"
numbersArray = [1, 10, 30, 50, 40, 33, 79]
average = 0
sum = 0
i = 0
j = 0
for i in numbersArray:
    print("i:", i)
    sum += i
    j += 1
    print("sum:", sum)
average = sum/j
print("average =", average)
myfile = open(file_name, "w")
for i in numbersArray:
    myfile.write(str(i) + "\n")
myfile.close()
print("""\nEven though we have already created the code to calculate the average, I am going
to repeat the process to use the numbers read from the data2.txt file that was created just to
make sure the code I write works properly.""")
average = 0
myfile = open(file_name, "r")
line_checked = myfile.readline()
print("first line_checked, outside the while loop: ")
sum = int(line_checked)
count = 1
while line_checked != "":
    line_checked = myfile.readline()
    if(line_checked != ""):
        # print("Inside while loop and if statement") # commented out as only needed to check
        sum += int(line_checked)
        # print("sum:", sum)
        count += 1
        # print("count:", count)
average = sum/count
print("\nThe AVERAGE =", average)