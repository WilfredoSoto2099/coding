import tkinter as tk
import time
import json
import os

def load_authorized_vehicles(filename='authorized_vehicles.json', directory=r'C:\coding\Coding project'):
    filepath = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_authorized_vehicles(authorized_vehicles, filename='authorized_vehicles.json', directory=r'C:\coding\Coding project'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    authorized_vehicles.sort()
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(authorized_vehicles, file, indent=4)

def print_authorized_vehicles():
    vehicles = load_authorized_vehicles()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, 'Printing all Authorized Vehicles...\n')
    root.update()
    display_vehicles_slowly(vehicles, 0)

def check_authorized_vehicle():
    vehicles = load_authorized_vehicles()
    display_vehicles_slowly(vehicles, 0)

def display_vehicles_slowly(vehicles, index):
    if index < len(vehicles):
        vehicle = vehicles[index]
        output_text.insert(tk.END, f"{vehicle}\n")
        root.update()
        # Repeat function after 1 second (1000 milliseconds)
        root.after(1000, lambda: display_vehicles_slowly(vehicles, index + 1))

def add_authorized_vehicle():
    vehicles = load_authorized_vehicles()

    def add_vehicle():
        new_vehicle = input_field.get().strip().upper()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, 'Adding vehicle...\n')
        root.update()
        time.sleep(2)
        vehicles.append(new_vehicle)
        save_authorized_vehicles(vehicles)
        output_text.insert(tk.END, f'{new_vehicle} has been added to the Authorized Vehicle list.\n')
        input_field.delete(0, tk.END)
        wait_for_user_input()
        output_text.delete(1.0, tk.END)
        submit_button.pack_forget()

    input_field.delete(0, tk.END)
    input_field.insert(0, 'Enter vehicle name...')
    submit_button.config(command=add_vehicle)
    submit_button.pack(pady=10)

def remove_authorized_vehicle():
    vehicles = load_authorized_vehicles()

    def remove_vehicle():
        vehicle_to_remove = input_field.get().strip().upper()
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, 'Removing vehicle...\n')
        root.update()
        time.sleep(2)
        if vehicle_to_remove in vehicles:
            vehicles.remove(vehicle_to_remove)
            save_authorized_vehicles(vehicles)
            output_text.insert(tk.END, f'{vehicle_to_remove} has been removed from the Authorized Vehicle list.\n')
        else:
            output_text.insert(tk.END, f'{vehicle_to_remove} was not found in the list of authorized vehicles.\n')
        input_field.delete(0, tk.END)
        wait_for_user_input()
        output_text.delete(1.0, tk.END)
        submit_button.pack_forget()

    input_field.delete(0, tk.END)
    input_field.insert(0, 'Enter vehicle name...')
    submit_button.config(command=remove_vehicle)
    submit_button.pack(pady=10)

def clear_output():
    output_text.delete(1.0, tk.END)

def wait_for_user_input():
    continue_button = tk.Button(root, text="Continue", command=lambda: continue_button.pack_forget())
    continue_button.pack(pady=10)
    root.wait_window(continue_button)

def exit_program():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, 'Exiting program...\n')
    root.update()
    time.sleep(2)
    root.destroy()

# Setting up the GUI
root = tk.Tk()
root.title("AutoCountry Vehicle Finder 0.1")

header_label = tk.Label(root, text='AutoCountry Vehicle Finder 0.1\n********************************\nPlease choose an option below:', font=('Arial', 14))
header_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

print_button = tk.Button(button_frame, text="1. Print all Authorized Vehicles", command=print_authorized_vehicles)
print_button.grid(row=0, column=0, padx=5, pady=5)

check_button = tk.Button(button_frame, text="2. Check if a Vehicle is Authorized", command=check_authorized_vehicle)
check_button.grid(row=1, column=0, padx=5, pady=5)

add_button = tk.Button(button_frame, text="3. Add a Vehicle to the Authorized List", command=add_authorized_vehicle)
add_button.grid(row=2, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="4. Remove a Vehicle from the Authorized list", command=remove_authorized_vehicle)
remove_button.grid(row=3, column=0, padx=5, pady=5)

exit_button = tk.Button(button_frame, text="5. Exit", command=exit_program)
exit_button.grid(row=4, column=0, padx=5, pady=5)

input_field = tk.Entry(root, width=50)
input_field.pack(pady=10)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

submit_button = tk.Button(root, text="Submit")
submit_button.pack_forget()

root.mainloop()
