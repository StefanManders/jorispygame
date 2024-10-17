import pygame

# Initialiseer Pygame
pygame.init()

# Scherm afmetingen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Kleuren
white = (255, 255, 255)
black = (0, 0, 0)

# Instellen van de klok voor framerate
clock = pygame.time.Clock()

# Lettertype instellen
font = pygame.font.Font(None, 74)

# Positie van de tekst
text_x = 0
text_y = screen_height // 2 - 50

# Snelheid van de tekst
text_speed_x = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Scherm vullen met witte achtergrond
    screen.fill(white)

    # Tekst renderen
    text = font.render("Joris", True, black)
    
    # Tekst op het scherm tekenen
    screen.blit(text, (text_x, text_y))

    # Tekst laten bewegen
    text_x += text_speed_x

    # Als de tekst de rand van het scherm bereikt, omkeren
    if text_x > screen_width - text.get_width() or text_x < 0:
        text_speed_x = -text_speed_x

    # Update het scherm
    pygame.display.flip()

    # Frame rate instellen
    clock.tick(60)

# Sluit Pygame af
pygame.quit()

