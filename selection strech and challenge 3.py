#Matthew Wadkin
#01/10/14
#this program will change the date in the normal formt

date_input = input("Please enter a date in the format DD/MM/YY (must be between 1931 and 2030): ")
day = int(date_input[0] + date_input[1])
month = int(date_input[3] + date_input[4])
year = int(date_input[6] + date_input[7])

if day == 1:
    day = str(day) + "st"
elif day == 2:
    day = str(day) + "nd"
elif day == 3:
    day = str(day) + "rd"
elif day = 21:
    day = str(day) + "st"
elif day = 22:
    day = str(day) + "nd"
elif day = 23:
    day = str(day) + "rd"
elif day = 31:
    day = str(day) + "st"
else:
    day = str(day) + "th"

if month == 1:
    month = "January"
elif month == 2:
    month = "Febuary"
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
else:
    month = "December"

if year > 30:
    year = "19" + str(year)
else:
    year = "20" + str(year)

print("The date you entered is: {0} {1} {2}".format(day,month,year))
