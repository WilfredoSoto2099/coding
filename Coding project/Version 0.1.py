import time #time delay module

#Header
def display_header():
    header = '********************************\n'
    header += 'AutoCountry Vehicle Finder 0.1\n'
    header += "********************************\n"
    header += 'Please Enter the following number below from the following menu\n'
    header += '\n'
    header += '1. Print all Authorized Vehicles\n'
    header += '2. Exit\n'
    print(header)

#List of authorized vehicles 
authorized_vehicles = [
    "Ford F-150",
    "Chevrolet Silverado",
    "Tesla CyberTruck",
    "Toyota Tundra",
    "Nissan Titan"
]
#Module to define user input
def handle_user_choice():
    while True:
        try:
            choice = int(input('Enter your choice (1 or 2): ')) #choices
            if choice == 1:
                print('Printing all Authorized Vehicles...') #prints vehicle
                time.sleep(2) #delay
                print () #adds a space
                for vehicle in authorized_vehicles: #pulls up authorized vehicle menu
                    print(f'*{vehicle}') #prints what's inside
                    time.sleep(1) # delay between inputs
                    print() # space between input
                time.sleep(5) #delay
                display_header() #display header again / repeats
            elif choice == 2: #ends program
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
                break #end loop
            else:
                print('Invalid choice. Please enter 1 or 2.') #wrong choice
        except ValueError:
            print('Invalid input. Please enter a valid number.') #prints answer for wrong choice

# Display the header once
display_header()

# Handle the user choice
handle_user_choice()
