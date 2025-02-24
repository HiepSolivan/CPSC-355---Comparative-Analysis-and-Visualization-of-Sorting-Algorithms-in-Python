import pygame

pygame.init()

# Visualizer window
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CPSC 355 Comparative Analysis and Visualization of Sorting Algorithms in Python')

# Initialize graphics
# Make some buttons for the user to start the visualization process (Made them too big so scale them)
# Source: https://www.youtube.com/watch?v=G8MYGDf_9ho
start_button_img = pygame.image.load('Graphics/Start Visualization.png').convert_alpha()
start_button_img = pygame.transform.scale(start_button_img, (320, 240))

pause_button_img = pygame.image.load('Graphics/Pause Visualization.png').convert_alpha()
pause_button_img = pygame.transform.scale(pause_button_img, (320, 240))

reset_button_img = pygame.image.load('Graphics/Reset Visualization.png').convert_alpha()
reset_button_img = pygame.transform.scale(reset_button_img, (320, 240))

# Class for buttons
class Button():
    def __init__(self, x_cord, y_cord, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_cord, y_cord)

    def draw(self):
        # Draw the button onto the surface starting at the top left
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Create instances of graphics
start_button = Button(100, 50, start_button_img)
pause_button = Button(100, 250, pause_button_img)
reset_button = Button(100, 450, reset_button_img)

# TODO: Implement visualization_tool which calls the various sorts + searches then makes visualization of the process

# Visualizer game loop
running = True
while running:
    screen.fill((255, 255, 255))

    start_button.draw()
    pause_button.draw()
    reset_button.draw()


    #Event handler: Quit when X clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()