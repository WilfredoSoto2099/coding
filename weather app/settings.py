# settings.py

import pygame
import os
from mapbox import Geocoder

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def get_city_from_map(screen, font, map_image, mapbox_api_key):
    map_rect = map_image.get_rect(topleft=(20, 100))
    geocoder = Geocoder(access_token=mapbox_api_key)
    dragging = False
    offset_x = 0
    offset_y = 0

    def closest_city(lat, lon):
        response = geocoder.reverse(lon=lon, lat=lat)
        if response.status_code == 200:
            features = response.geojson()['features']
            if features:
                return features[0]['place_name']
        return None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = map_rect.x - mouse_x
                    offset_y = map_rect.y - mouse_y
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    map_rect.x = mouse_x + offset_x
                    map_rect.y = mouse_y + offset_y
            if event.type == pygame.MOUSEBUTTONDOWN and not dragging:
                if map_rect.collidepoint(event.pos):
                    x, y = event.pos
                    lat = (y / screen.get_height()) * 180 - 90
                    lon = (x / screen.get_width()) * 360 - 180
                    city = closest_city(lat, lon)
                    if city:
                        return city

        screen.fill((185, 239, 255))
        screen.blit(map_image, map_rect)
        draw_text("Click on the map to select a city", font, (0, 0, 0), screen, 20, 20)
        pygame.display.flip()

def save_city(city):
    settings_dir = os.path.dirname(__file__)
    city_file_path = os.path.join(settings_dir, 'city.txt')
    with open(city_file_path, 'wb') as f:
        f.write(city.encode('utf-8'))

def load_city():
    settings_dir = os.path.dirname(__file__)
    city_file_path = os.path.join(settings_dir, 'city.txt')
    try:
        with open(city_file_path, 'rb') as f:
            return f.read().decode('utf-8').strip()
    except FileNotFoundError:
        return 'Tokyo'  # Default city