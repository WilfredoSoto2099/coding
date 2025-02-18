import subprocess
import sys
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Weather App Installer')
root.geometry('400x300')

label = tk.Label(root, text='Weather App Installer')
label.pack(pady=20)

# List of packages to install
packages = ['pygame', 'requests', 'mapbox', 'pygame_menu']

# Create a progress bar
progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress.pack(pady=20)

# Function to install packages and run the script
def install_and_run(packages):
    progress['maximum'] = len(packages)
    for i, package in enumerate(packages, start=1):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        progress['value'] = i
        root.update_idletasks()  # Update the progress bar
    # Path to your Weather app script
    script_path = 'weather_app.py'  # Ensure this path is correct
    subprocess.run(['python', script_path])
    root.destroy()  # Closes the window

# Button to start the installation and run the script
install_button = tk.Button(root, text='Install Packages', command=lambda: install_and_run(packages))
install_button.pack(pady=20)

root.mainloop()