import pygame

pygame.init()

# Initialize graphics

# Visualizer window
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Visualizer game loop
running = True
while running:
    #Event handler: Quit when X clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()