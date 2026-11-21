import pygame

pygame.init()
# Create the display surface object of specific dimension.
window = pygame.display.set_mode((500, 600))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
RED = (255, 0, 0)
BLUE=(0, 0, 255)
# Draw solid circle
pygame.draw.circle(window, RED, (400, 400), 60)
# Draw outlined circle
pygame.draw.circle(window, BLUE, (200, 200), 70, 4)
# Draws the surface object to the screen.
pygame.display.update()
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()