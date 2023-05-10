import pygame
import math


# Constants
WIDTH, HEIGHT          = 1200, 600
x1, x2                 = 1000, 0.1
k, b, m                = 2,0, 1
h                      = 0.001


# Initialize pygame
pygame.init()
pygame.display.set_caption("Péndulo Simple")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#Colores
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( WHITE )

    x1=x1+h*x2
    x2=x2+h*(-(k/m)*x1-(b/m)*x2)

    pygame.draw.circle(screen, BLACK, (x1, HEIGHT//2), 25 )
    
    if x1 > WIDTH - 25 or x1 < 0 + 25:
        x2 = -x2
     
    pygame.display.flip()
    

# Quit pygame
pygame.quit()