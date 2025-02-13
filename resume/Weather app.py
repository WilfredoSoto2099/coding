import pygame
import requests

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
    api_key = 'a6dd418f293f9e59f07ea0701cc7ac5d'  # Your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city + '&appid=' + api_key
    response = requests.get(complete_url)
    return response.json()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen color
    screen.fill((185, 239, 255))

    # Fetch weather data
    weather_data = get_weather('Tampa')  # Replace 'Tokyo' with your desired city
    if weather_data['cod'] == 200:
        main = weather_data['main']
        temperature = main['temp'] - 273.15  # Convert from Kelvin to Celsius
        weather_desc = weather_data['weather'][0]['description']

        # Display weather data
        font = pygame.font.Font(None, 36)
        text = font.render(f'Temperature: {temperature:.2f}°C', True, (0, 0, 0))
        screen.blit(text, (20, 20))
        text = font.render(f'Description: {weather_desc}', True, (0, 0, 0))
        screen.blit(text, (20, 60))

    # Display update
    pygame.display.flip()

# Quit weather app
pygame.quit()
