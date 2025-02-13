# settings.py

import pygame
import os

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def get_city_from_map(screen, font, map_image):
    map_rect = map_image.get_rect(topleft=(20, 100))
    cities = {
        "Tokyo": (139.6917, 35.6895),
        "New York": (-74.0060, 40.7128),
        "London": (-0.1276, 51.5074),
        "Paris": (2.3522, 48.8566),
        "Sydney": (151.2093, -33.8688),
        # Add more cities with their approximate coordinates
    }

    def closest_city(x, y):
        min_dist = float('inf')
        closest = None
        for city, (cx, cy) in cities.items():
            dist = (cx - x) ** 2 + (cy - y) ** 2
            if dist < min_dist:
                min_dist = dist
                closest = city
        return closest

    dragging = False
    offset_x = 0
    offset_y = 0

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
                    return closest_city(x, y)

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