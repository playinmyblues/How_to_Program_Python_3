# This file works on the exercise presented at the end of the chapter. See it below:

# TO USE SHORTCUT KEYS TO RUN THE PROGRAM IN PYCHARM CE ON A MAC, USE the keys ^R. On a Mac
# keybaord that is the Ctrl key (Ctrl and ^ are on the key together) and R.
# On the Logitech K400 keybaord that is Ctrl-R.

#Exercise at the end of the chapter:
#Modify the program developed in this lecture to also keep track of the chance
#that there will be rain on the particular day. Below are a few hints if you
#need them.
#◊ You already are reading in the data you need to.
#◊ You will need to add some additional lines to the analysis and presentation
#parts of the code.
#◊ Keep track of how many days had rain as you go through the list “gooddata.”
#◊ Compute a percentage of days with rain and report that.

# My adaptation to work with the data that I have for the weather in New Glasgow will be to have
# a look at the average temperature to see if it goes above a certain value. Also, take the high
# temperature and determine how many days goes above a certain value. Once you start thinking about
# what might be relevant to weather information, you can start to figure out other things to do with
# the data to process it in relevant ways. You might do something such as take the highest
# temperature in August in previous years and determine if any day in August of the current year is
# above that highest temperature.

# The section of code below that processes the data will be different from the previous Python
# programs's code.

# Because I used data I obtained from a website that did not contain the exact same categories of
# data in the chapter, I have to make up my own criteria for this exercise. I should also take the
# lead from the exercise though, which is to actually edit the code presented in the chapter so that
# the rest of the file is processed and now the purpose of the program is better suits the original
# intent. The code presented did not quite fully work through the whole process and that was left
# for the reader to do in the exercise.

########## Read in Data ##########
# Open File
# Read lines from file
# Close file
########## Analyze Data ##########
########## Present Results ##########

# After finding a website to give me data on temperatures for New Glasgow, NS, I can only get them
# as far back as July 9, 2025 from that particular site:
# https://newglasgow.weatherstats.ca/charts/temperature-daily.html
# I am going to use the month of August. And I am changing the data to be read to what I can get
# from that site: Date, Max Temp, Hourly Mean Temp, Mean of Min/MAx Temp, Min Temp

########## Read in Data ##########
# Open File
external_file = input("Enter the name of the data file: ")
# At this point, the name of the external file is too long. I am shortening it to t4.csv
infile = open(external_file, 'r')
#Read lines from File
datalist = []
for line in infile:
    #get data from line
    date, maxt, meant, mean_min_max, mint = line.split(',')
    lowtemp = float(mint[0:3])
    hightemp = float(maxt[0:3])
    avg_temp = float(meant[0:3])
    avg_min_max_temp = float(mean_min_max[0:3])
    # The PDF shows the use of a / as the delimiter for the date. My file uses a -.
    # And I changed the order of the date to work with the output that my spreadsheet app does
    y, m, d = date.split("-")
    year = int(y)
    month = int(m)
    day = int(d)
    #Put data into list
    datalist.append([day, month, year, lowtemp, hightemp, avg_temp, avg_min_max_temp])
    print(datalist)
#Close File
# This is the simple command on the line below
infile.close()
########## Analyze Data ##########
# The content continues on from here with something simple and probably will not require changing
# the code above. However, that may prove to be different as I continue to work through it. It
# could be that I need to change something above because I did something different that what is
# presented in the PDF. Or there could be another reason.

# Get date of interest
month = int(input("For the date you care about, enter the month (1 - 12): "))
day = int(input("For the date you care about, enter the day (1 - 31): "))
# The year is not needed as they are all from 2025 this time.
# Find historical data for date
# Also add field [6] to gooddata
gooddata = []
for single_day in datalist:
    print("single_day: ", single_day)
    if(single_day[0] == day) and (single_day[1] == month):
        gooddata.append([single_day[3],
                         single_day[4], single_day[5], single_day[6]])
print("gooddata: ", gooddata)

# Perform analysis
# I think that it would be useful with this dataset to find the average high temperature for the
# month and then list the days for which the high temperature was above the average high temperature.
# The temperature for those days should also be listed with that information.

min_so_far = 100        # Setting a value higher than the expected minimum temperature ensures
                        # the value to change. The same is true in the opposite way for the max
max_so_far = -100
num_good_dates = 0
sum_of_min = 0
sum_of_max = 0
sum_of_avg = 0
for single_day in gooddata:
    num_good_dates += 1
    sum_of_min += single_day[0]
    sum_of_max += single_day[1]
    sum_of_avg += single_day[2]
    if single_day[0] < min_so_far:
        print("min_so_far: ", min_so_far, single_day[0])
        min_so_far = single_day[0]
    if single_day[1] > max_so_far:
        max_so_far > single_day[1]
avg_low = sum_of_min / num_good_dates
avg_high = sum_of_max / num_good_dates
########## Present Results ##########
print("There were ", num_good_dates, " days")
print("The lowest temperature on record was ", min_so_far, " degrees C")
print("The highest temperature on record was ", max_so_far, " degrees C")
print("The average low has been ", avg_low, " degrees C")
print("The average high has been ", avg_high, " degrees C")

# At this point, I am going to keep the above code and start again for gooddata
#gooddata = []
print("gooddata:", gooddata)
# Now to check to see if the high temperature for a specific day was above or below the average
# high temperature for the month.
days_in_month = 0
sum_of_high = 0.0
for single_day in datalist:
    print("single_day: ", single_day)
    # I could put this code in the loop above that creates datalist but it will be here
    sum_of_high += single_day[4]
    days_in_month += 1
    if (single_day[0] == day):
        gooddata = single_day

print("gooddata: ", gooddata)
print("sum_of_high:", sum_of_high)
avg_high_temp = sum_of_high/days_in_month
th_month_string = str(month) + "th month"
print("The average high temperature for the", str(month) + "th month is:", avg_high_temp)
print("Alternate way of printing the above:")
print("The average high temperature for the " + th_month_string + " is: " + str(avg_high_temp))

# Let's try working with the list of lists
print("All of the first list of lists at [0][0]:", datalist[0][4])
days_high_temp = gooddata[4]
if (days_high_temp >= avg_high_temp):
    # To break a long line of code into multiple lines, end a line with a \
    # However, that adds a tab for me.
    # I can also just put a closing quote at the end of the line, start a new line and start that
    # quotes and continue on as normal.
    print("The high temperature of", days_high_temp, "deg C is higher than the average"
          " temperature of", avg_high_temp, " deg C.")
elif (days_high_temp == avg_high_temp):
    print("The high temperature of", days_high_temp, "deg C is equal to the average"
          " temperature of", avg_high_temp, "deg C.")
else:
    print("The high temperature of", days_high_temp, "deg C is less than the average"
          " temperature of", avg_high_temp, "deg C.")
# IT TOOK ME A LONG TIME TO SORT ALL OF THIS OUT. THERE WAS A LOT OF THINKING ABOUT WHAT EXACTLY
# I WAS WORKING WITH AND FINDING OUT THAT I WAS WORKING WITH SOMETHING DIFFERENT. THIS WAS BECAUSE
# I WAS WORKING WITH LISTS - ARRAYS OF ARRAYS OF DATA AND I WAS TRYING TO PULL OUT DATA FROM THAT
# AND WAS NOT THINKING ABOUT IT CLEARLY.
print("More testing\
      of using\
      a backslash.")
print("Another line\
 but now I am putting the text just about next to the side of the window.")