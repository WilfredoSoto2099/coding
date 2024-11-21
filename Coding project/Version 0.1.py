import time

def display_header():
    header = '********************************\n'
    header += 'AutoCountry Vehicle Finder 0.1\n'
    header += "********************************\n"
    header += 'Please Enter the following number below from the following menu\n'
    header += '\n'
    header += '1. Print all Authorized Vehicles\n'
    header += '2. Exit\n'
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
        try:
            choice = int(input('Enter your choice (1 or 2): '))
            if choice == 1:
                print('Printing all Authorized Vehicles...')
                time.sleep(2)
                print ()
                for vehicle in authorized_vehicles:
                    print(f'*{vehicle}')
                    time.sleep(1)
                    print()
                time.sleep(5)
                display_header()
            elif choice == 2:
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
                break
            else:
                print('Invalid choice. Please enter 1 or 2.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

# Display the header once
display_header()

# Handle the user choice
handle_user_choice()
