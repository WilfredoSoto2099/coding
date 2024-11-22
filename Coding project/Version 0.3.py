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
    header += '4. Exit\n'
    print(header)

authorized_vehicles = [
    "Ford F-150",
    "Chevrolet Silverado",
    "Tesla CyberTruck",
    "Toyota Tundra",
    "Nissan Titan"
]

def handle_user_choice():
    while True:
        display_header()
        try:
            time.sleep(2) #readability
            choice = int(input('Enter your choice (1, 2, 3, or 4): ')) #user inp
         #first choice
            if choice == 1: 
                print() #readability
                print('Printing all Authorized Vehicles...') #readability/answer
                time.sleep(2) #readability
                for vehicle in authorized_vehicles:
                    print()  # Adds a new line for better readability
                    time.sleep(1) #read
                    print(vehicle) #print dictonary
                print() #readability
        #second choice
            elif choice == 2:
                uservehicle = input('Please Enter the full vehicle name:').strip().lower() #user inp
                if uservehicle in [vehicle.lower() for vehicle in authorized_vehicles]:
                    time.sleep(1) #readability
                    print(f'{uservehicle} is an authorized vehicle') #answer
                else:
                    time.sleep(1) #readability
                    print(f'{uservehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again...') #answer
                print() #readability
            elif choice == 3:
        #third choice
                addvehicle = input('Please insert the vehicle name you would like to add: ').strip() #user inp
                authorized_vehicles.append(addvehicle) #add userinput to dictonary 
                time.sleep(1) #readability
                print('Loading...') #readability/answer
                time.sleep(3) #readability
                print(f'{addvehicle} has been added to the Authorized Vehicle list.') #answer
                print() #readability
            elif choice == 4:
        #fourth choice
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!') #end 
                break  # Exit the loop and end the program
            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.') #answer
                print() #readability
            time.sleep(2) #readability
            continue_choice = input('Would you like to continue? (yes/no): ').strip().lower() #userinp
            if continue_choice == 'Yes'.lower(): #no case sensitive
                print('Loading...') #answer
                time.sleep(3) #readability
                continue  # Restart the loop
            else:
                time.sleep(1) #readability
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!') #end 
                break  # Exit the loop and end the program
        except ValueError:
            time.sleep(1)
            print('Invalid input. Please enter a valid number.')
            print()

# Start the user choice handling loop
handle_user_choice()
