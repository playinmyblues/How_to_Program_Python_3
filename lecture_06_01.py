# This covers material from lecture 6 in the course - Files and Strings.
# The next line is a typial command to read from the input.txt file. But if it does not exist, it
# will produce and error. Delete the input.txt file from the directory and see what happens.
myfile = open("input.txt", "r")

# Read input from MyDataFile.txt
# Write output to results.txt
infile = open("MyDataFile.txt", "r")
outfile = open("results.txt", "w")
# From writing the code, running it, it is seen that results.txt is still empty but it was created.
# Now, we need to close the files.
infile.close()
outfile.close()

# Here are two options for dealing with files, the second way is said to be safer:
####### Option 1
myfile = open("Filename", "r")
# Do something here
myfile.close()

####### Option 2 - This automatically closes the file. But the file is only open for the section
# of code that is indented in the code block
with open("Filename", "w") as myfile:
    # Do something here
    print("1") # code just to do something, otherwise, an error is thrown

# To use the with thing with an example of an infile and an outfile, you should nest the statements
# I needed to create the infile first.
with open("infile", "r") as my_infile:
    with open("outfile", "w") as my_outfile:
        # write code here
        print("1") # just to have code

# Here is an example of code to create something in the file.
myfile = open("test_file.txt", "w")
myfile.write("This line is written to the file.")
myfile.close()
# And checking the directory shows the file was created and written to.
# WHEN WE USE this write command, we can only write out strings.
# Here is more code showing different things you can do:
myfile = open("test_file.txt", "a")
to_write = "The number of countries is " + str(196)
myfile.write(to_write)
myfile.close()
# 13:07 in video

# The write command does not add a newline character. If you want a new line for each line of
# text, you have to add it yourself when you use the write command.
# Here is an example:
# I will create volume1 and volume2
volume1 = 12345
volume2 = 678910
with open("results.txt", "w") as outfile:
    outfile.write("The first volume is " + str(volume1) + '\n')
    outfile.write("The second volume is " + str(volume2) + '\n')
# The first time I wrote this code, I made volume1 and volume2 strings. They would not have to be
# cast as strings again. Integers and floats and probably booleans would have to be cast as strings
# Let's try more:
volume3 = True
volume4 = False
volume5 = 56.23
# Note the use of "a" to append to the file as it was already created with the previous command
with open("results.txt", "a") as outfile:
    outfile.write("The third volume is " + str(volume3) + '\n') # removing str throws an error
    outfile.write("The fourth volume is " + str(volume4) + '\n')
    outfile.write("The fifth volume is " + str(volume5) + '\n')
# Video at 14:57