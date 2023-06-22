import pygame
import math


# Constants
WIDTH, HEIGHT          = 1200, 600
x1, x2                 = 1000, 0.1
<<<<<<< HEAD
k, b, m                = 2, 0.1, 1
=======
<<<<<<< HEAD
k, b, m                = 2,1, 1
=======
k, b, m                = 2,0.5, 1
>>>>>>> b361a8c57d36f3c50e4d339996fd8400a518cce0
>>>>>>> ee3e8f9dc345ffff628e3ef3c67901c04f9455e6
h                      = 0.001




# Initialize pygame
pygame.init()
pygame.display.set_caption("Masa Resorte Amortiguador")
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )


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

    pygame.draw.circle(screen, BLACK, (x1, HEIGHT//2), 15 )
    
    if x1 > WIDTH - 25 or x1 < 0 + 25:
        x2 = -x2
     
    pygame.display.flip()
    

# Quit pygame
pygame.quit()