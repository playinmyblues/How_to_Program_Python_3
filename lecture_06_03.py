# This file starts by showing how to read a text file in complete with one command. The resulting
# string is assigned to a variable and after that, it can be manipulated. Such a manipulation
# would probably involve breaking that string into smaller strings.
myfile = open("results.txt", "r")
line_from_file = myfile.read()      # reading the whole file at once
myfile.close()
# This next line is just for me to see what the result is from the current code.
print(line_from_file)
# The above line of code prints the file just as the original file is stored. Each line ends and
# the string has a new line in it and is printed just as the original file looks.

# Python can handle files as binary data as well. From the commands provided in the lecture, I
# think what is presented actually uses text files but deals with the data in binary format. See
# the commands below for writing, appending, and reading a file - note that the commands are similar
# to those of dealing with text files as strings.
# Write:    myfile = open("filename", "wb")     - wb is the similar but binary version
# Append:   myfile = open("filename", "ab")
# Read:     myfile = open("filename", "rb")
# I could be wrong in a way as all files stored on the computer are actually in binary format
# despite how we see them presented in a file finder or file manager app that allows us to
# browse and manipulate the files on a computer.
# Pickle is a module that can be used with Python to make using binary files easier.
# Let's try a little experiment
myfile = open("results.txt", "rb")
line_from_file_binary = myfile.readline()
print(line_from_file_binary)
# That did not work as expected. Run the program to see the result - not a series of 0's and 1's.
# On the web, on the Python website it says Pickle is automatically installed with Python3. Here
# is an example that shows the version of Pickle:
import pickle
print(pickle.format_version)    # Found this from a websearch, not the Python3 website
# More to be explored later!