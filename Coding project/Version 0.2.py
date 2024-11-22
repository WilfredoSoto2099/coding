import time

def display_header():
    time.sleep(2)
    header = '********************************\n'
    header += 'AutoCountry Vehicle Finder 0.1\n'
    header += "********************************\n"
    header += 'Please Enter the following number below from the following menu\n'
    header += '\n'
    header += '1. PRINT all Authorized Vehicles\n'
    header += '2. SEARCH for Authorized Vehicle\n'
    header += '3. Exit\n'
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
            choice = int(input('Enter your choice (1, 2 or 3): '))
            if choice == 1:
                print('Printing all Authorized Vehicles...')
                time.sleep(2)
                for vehicle in authorized_vehicles:
                    print() # Adds a new line for better readability
                    time.sleep(1)
                    print(vehicle)
            elif choice == 2:
                uservehicle = input('Please Enter the full vehicle name:').strip().lower()
                if uservehicle in [vehicle.lower() for vehicle in authorized_vehicles]:
                    time.sleep(1)
                    print(f'{uservehicle} is an authorized vehicle')
                else:
                    time.sleep(1)
                    print(f'{uservehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again...')
                time.sleep(1)
            if choice == 3:
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
                break  # Exit the loop and end the program
        except ValueError:
            print('Invalid input. Please enter a valid number.')

# Start the user choice handling loop
handle_user_choice()
