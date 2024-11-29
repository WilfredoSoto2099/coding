import time

def display_header():
    print()
    header = '********************************\n'
    header += 'AutoCountry Vehicle Finder 0.1\n'
    header += "********************************\n"
    header += 'Please Enter the following number below from the following menu\n'
    header += '\n'
    header += '1. Print all Authorized Vehicles\n'
    header += '2. Check if a Vehicle is Authorized\n'
    header += '3. Add a Vehicle to the Authorized List\n'
    header += '4. Remove a Vehicle from the Authorized list\n'
    header += '5. Exit\n'
    time.sleep(1)
    print(header)

#list of authorized vehicles 
authorized_vehicles = [ 
    "FORD F-150",
    "CHEVORLET SILVERADO",
    "TESLA CYBERTRUCK",
    "TOYOTA TUNDRA",
    "NISSAN TITAN"
]

def handle_user_choice():
    while True:
        display_header()
        try:
            time.sleep(1) # readability
            choice = int(input('Enter your choice (1, 2, 3, 4, or 5): ')) # user input
            # first choice
            if choice == 1: 
                print() # readability
                print('Printing all Authorized Vehicles...') # readability/answer
                time.sleep(2) # readability
                for vehicle in authorized_vehicles:
                    print()  # Adds a new line for better readability
                    time.sleep(1) # readability
                    print(vehicle) # print dictionary
                print() # readability
            # second choice
            elif choice == 2:
                user_vehicle = input('Please Enter the full vehicle name: ').strip().lower() # user input
                if user_vehicle in [vehicle.lower() for vehicle in authorized_vehicles]:
                    time.sleep(1) # readability
                    print(f'{user_vehicle} is an authorized vehicle') # answer
                else:
                    time.sleep(1) # readability
                    print(f'{user_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again...') # answer
                print() # readability
            # third choice
            elif choice == 3:
                add_vehicle = input('Please insert the vehicle name you would like to add: ').upper() # user input
                authorized_vehicles.append(add_vehicle) # add user input to dictionary 
                time.sleep(1) # readability
                print('Loading...') # readability/answer
                time.sleep(3) # readability
                print(f'{add_vehicle} has been added to the Authorized Vehicle list.') # answer
                print() # readability
            # fourth choice
            elif choice == 4:
                remove_vehicle = input('Please insert the vehicle name you would like to remove: ').upper()
                if remove_vehicle in authorized_vehicles:
                    authorized_vehicles.remove(remove_vehicle) # remove user input from dictionary
                    time.sleep(1) #readabiltiy
                    print('Loading...') #readability
                    time.sleep(3) #readability
                    continue_choice = input(f'Are you sure you want to remove {remove_vehicle} from the Authorized Vehicles List?').strip() #user input
                    if continue_choice == 'yes': #loop for choice
                        print('Loading...') #readability
                        time.sleep(2)
                        print(f'{remove_vehicle} HAS been removed from the Authorized Vehicle list.') #answer
                        print() #readability
                    else:
                        print() #readability
                        time.sleep(1) #readability
                        print(f'{remove_vehicle} has NOT been removed from the Authorized Vehicles list') #answer
                        continue  #continues the loop
                else:
                    time.sleep(1) #readability
                    print('Loading...') #readability
                    time.sleep(1) #readability
                    print(f'{remove_vehicle} was not found in the list of authorized vehicles.') #answer
                    print() #readability
                    time.sleep(2) #readabiltiy
            # fifth choice
            elif choice == 5:
                time.sleep(1) # readabiltiy
                print() #readability
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!') # end 
                print() #readability
                break  # Exit the loop and end the program
            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.') # answer
                print() # readability
            time.sleep(2) # readability
            continue_choice = input('Would you like to continue? (yes/no): ').strip().lower() # user input
            if continue_choice == 'yes': # no case sensitive
                print('Loading...') # answer
                print()
                print()
                time.sleep(3) # readability
                continue  # Restart the loop
            else:
                time.sleep(1) # readability
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!') # end 
                print()
                print()
                break  # Exit the loop and end the program
        except ValueError:
            time.sleep(1)
            print('Invalid input. Please enter a valid number.')
            print()

# Start the user choice handling loop
handle_user_choice()
