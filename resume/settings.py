import pygame

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def get_city_input(screen, font):
    input_active = False
    user_text = ''
    input_box = pygame.Rect(20, 100, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_inactive = pygame.Color('gray15')
    color = color_inactive

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        return user_text
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        screen.fill((185, 239, 255))
        color = color_active if input_active else color_inactive
        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(user_text, font, (0, 0, 0), screen, input_box.x + 5, input_box.y + 5)
        input_box.w = max(200, font.size(user_text)[0] + 10)
        pygame.display.flip()