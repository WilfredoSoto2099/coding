import time
import json
import os

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
    print(header)

def load_authorized_vehicles(filename='authorized_vehicles.json', directory=r'C:\coding\Coding project'):
    filepath = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    print() # readability
    print(f"Loading from: {filepath}")  # Debugging: Print the file path being loaded
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_authorized_vehicles(authorized_vehicles, filename='authorized_vehicles.json', directory=r'C:\coding\Coding project'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    authorized_vehicles.sort()  # Sort the list alphabetically before saving
    filepath = os.path.join(directory, filename)
    print() #readibility
    print()
    print(f"Saving to: {filepath}")  # Debugging: Print the file path being saved
    print() #readability
    with open(filepath, 'w') as file:
        json.dump(authorized_vehicles, file, indent=4)

def handle_user_choice():
    authorized_vehicles = load_authorized_vehicles()
    
    while True:
        display_header()
        try:
            time.sleep(2)  # readability
            choice = int(input('Enter your choice (1, 2, 3, 4, or 5): '))  # user input
            # first choice
            if choice == 1:
                print()  # readability
                print('Printing all Authorized Vehicles...')  # readability/answer
                time.sleep(2)  # readability
                for vehicle in authorized_vehicles:
                    print()  # Adds a new line for better readability
                    time.sleep(1)  # readability
                    print(vehicle)  # print list
                print()  # readability
            # second choice
            elif choice == 2:
                user_vehicle = input('Please Enter the full vehicle name: ').strip().upper()  # user input
                if user_vehicle in [vehicle.upper() for vehicle in authorized_vehicles]:
                    time.sleep(1)  # readability
                    print(f'{user_vehicle} is an authorized vehicle')  # answer
                else:
                    time.sleep(1)  # readability
                    print(f'{user_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again...')  # answer
                print()  # readability
            # third choice
            elif choice == 3:
                print()
                add_vehicle = input('Please insert the vehicle name you would like to add: ').strip().upper()  # user input
                authorized_vehicles.append(add_vehicle)  # add user input to list
                save_authorized_vehicles(authorized_vehicles)  # save changes
                time.sleep(1)  # readability
                print() #readability
                print('Loading...')  # readability/answer
                print() #readability
                time.sleep(3)  # readability
                print(f'{add_vehicle} has been added to the Authorized Vehicle list.')  # answer
                print()  # readability
            # fourth choice
            elif choice == 4:
                remove_vehicle = input('Please insert the vehicle name you would like to remove: ').strip().upper()
                if remove_vehicle in authorized_vehicles:
                    confirmation = input(f'Are you sure you want to remove {remove_vehicle} from the Authorized Vehicles List? (yes/no): ').strip().lower()
                    if confirmation == 'yes':
                        authorized_vehicles.remove(remove_vehicle)  # remove user input from list
                        save_authorized_vehicles(authorized_vehicles)  # save changes
                        time.sleep(1)
                        print('Loading...')
                        time.sleep(3)
                        print(f'{remove_vehicle} has been removed from the Authorized Vehicle list.')
                        print()
                    else:
                        print(f'Removal of {remove_vehicle} canceled.')
                else:
                    print(f'{remove_vehicle} was not found in the list of authorized vehicles.')
                    time.sleep(2)
            # fifth choice
            elif choice == 5:
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')  # end
                break  # Exit the loop and end the program
            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.')  # answer
                print()  # readability
            time.sleep(2)  # readability
            continue_choice = input('Would you like to continue? (yes/no): ').strip().lower()  # user input
            if continue_choice == 'yes':  # no case sensitive
                print('Loading...')  # answer
                time.sleep(3)  # readability
                continue  # Restart the loop
            else:
                time.sleep(1)  # readability
                print() #readability
                print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')  # end
                break  # Exit the loop and end the program
        except ValueError:
            time.sleep(1)
            print('Invalid input. Please enter a valid number.')
            print()

# Start the user choice handling loop
handle_user_choice()
