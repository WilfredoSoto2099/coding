import pygame
import os
import requests
import pygame_menu
from settings import save_city, load_city, get_states_and_cities

# Initializing pygame
pygame.init()

# Set up resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption('Weather app')

# Function to get weather data
def get_weather(city):
    api_key = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city + '&appid=' + api_key
    response = requests.get(complete_url)
    return response.json()

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Main loop
running = True
city = load_city()  # Load the saved city
font = pygame.font.Font(None, 36)

# Create the settings menu
menu = pygame_menu.Menu('Settings', screen_width, screen_height, theme=pygame_menu.themes.THEME_BLUE)
states_and_cities = get_states_and_cities()

selected_state = None
selected_city = None

def set_state(value, state):
    global selected_state
    selected_state = state
    print(f"Selected state: {state}")
    city_selector.update([(city, city) for city in states_and_cities[state]])

def set_city(value, city):
    global selected_city
    selected_city = city
    print(f"Selected city: {city}")
    save_city(city)

state_selector = menu.add.dropselect('Select State: ', [(state, state) for state in states_and_cities.keys()], onchange=set_state)
city_selector = menu.add.dropselect('Select City: ', [(city, city) for city in states_and_cities['Alabama']], onchange=set_city)

# Define the settings button
settings_button = pygame.Rect(20, 150, 140, 32)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if settings_button.collidepoint(event.pos):
                menu.mainloop(screen)

    # Screen color
    screen.fill((185, 239, 255))

    # Fetch weather data
    weather_data = get_weather(city)
    if weather_data['cod'] == 200:
        main = weather_data['main']
        temperature = main['temp'] - 273.15  # Convert from Kelvin to Celsius
        weather_desc = weather_data['weather'][0]['description']

        # Display weather data
        draw_text(f'Temperature: {temperature:.2f}°C', font, (0, 0, 0), screen, 20, 20)
        draw_text(f'Description: {weather_desc}', font, (0, 0, 0), screen, 20, 60)

    # Settings button
    pygame.draw.rect(screen, (0, 0, 0), settings_button)
    draw_text('Settings', font, (255, 255, 255), screen, settings_button.x + 5, settings_button.y + 5)

    # Display update
    pygame.display.flip()

# Quit weather app
pygame.quit()