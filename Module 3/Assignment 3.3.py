# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
month = int(input('Please insert a month: '))
day = int(input('Please insert a day: '))
year = int(input('Please insert a year: '))
# Output: Valid date 
validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31


#validating input
if year <= MIN_YEAR: # invalid year
    validDate = False
elif month < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif day < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    # Output statement
    print(f'{month}/{day}/{year} is a valid date')
else:
    # Output statement
    print (f'{month}/{day}/{year} Is an invalid date')