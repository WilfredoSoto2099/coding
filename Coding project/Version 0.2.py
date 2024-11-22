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
            time.sleep(2)
            choice = int(input('Enter your choice (1, 2, 3, or 4): '))
            if choice == 1:
                print()
                print('Printing all Authorized Vehicles...')
                time.sleep(2)
                for vehicle in authorized_vehicles:
                    print()  # Adds a new line for better readability
                    time.sleep(1)
                    print(vehicle)
                print()
            elif choice == 2:
                uservehicle = input('Please Enter the full vehicle name:').strip().lower()
                if uservehicle in [vehicle.lower() for vehicle in authorized_vehicles]:
                    time.sleep(1)
                    print(f'{uservehicle} is an authorized vehicle')
                else:
                    time.sleep(1)
                    print(f'{uservehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again...')
                print()
            elif choice == 3:
                addvehicle = input('Please insert the vehicle name you would like to add: ').strip()
                authorized_vehicles.append(addvehicle)
                time.sleep(1)
                print('Loading...')
                time.sleep(3)
                print(f'{addvehicle} has been added to the Authorized Vehicle list.')
                print()
            elif choice == 4:
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
                break  # Exit the loop and end the program
            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.')
                print()
            time.sleep(2)
            continue_choice = input('Would you like to continue? (yes/no): ').strip().lower()
            if continue_choice == 'Yes'.lower():
                print('Loading...')
                time.sleep(3)
                continue  # Restart the loop
            else:
                time.sleep(1)
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
                break  # Exit the loop and end the program
        except ValueError:
            time.sleep(1)
            print('Invalid input. Please enter a valid number.')
            print()

# Start the user choice handling loop
handle_user_choice()
