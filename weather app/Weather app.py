import pygame
import os
import requests
from settings import draw_text, get_city_from_map, save_city, load_city

# Initializing pygame
pygame.init()

# Set up resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption('Weather app')

# Load world map image
map_image_path = os.path.join(os.path.dirname(__file__), 'world_map.png')
map_image = pygame.image.load(map_image_path)

# Function to get weather data
def get_weather(city):
    api_key = 'a6dd418f293f9e59f07ea0701cc7ac5d'  # Your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city + '&appid=' + api_key
    response = requests.get(complete_url)
    return response.json()

# Main loop
running = True
city = load_city()  # Load the saved city
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if settings_button.collidepoint(event.pos):
                new_city = get_city_from_map(screen, font, map_image)
                if new_city:
                    city = new_city
                    save_city(city)

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
    settings_button = pygame.Rect(20, 150, 140, 32)
    pygame.draw.rect(screen, (0, 0, 0), settings_button)
    draw_text('Settings', font, (255, 255, 255), screen, settings_button.x + 5, settings_button.y + 5)

    # Display update
    pygame.display.flip()

# Quit weather app
pygame.quit()
