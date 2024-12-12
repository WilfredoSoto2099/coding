
basecharge = 35.00
# Number of characters.
charcharge = 4.00
# Color of characters.
colorcharge = 15.00
# Type of wood.
oakcharge = 20.00
#user input
userchar = int(input('Insert how many characters will be on the sign: '))
usercolor = input('Insert what color you want: ').strip().lower()
userWoodtype = input('Do you want oak or pine sign?: ').strip().lower()

#initial base charge
charge = basecharge


# Write assignment and if statements here as appropriate.
#user color charge if statement
#User input character charge
if userchar > 5:
    charge += charcharge * (userchar - 5)
if usercolor == 'gold':
    charge += colorcharge
#user input wood charge
if userWoodtype == 'oak':
    charge += oakcharge

# Output Charge for this sign.
print(f"The charge for this sign is ${charge:.2f}")