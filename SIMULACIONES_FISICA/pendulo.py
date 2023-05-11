import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
X1 = math.pi / 2    # Posicion inicial del sistema de forma angular
X2 = 0.1            # Velocidad con la que comienza el movimiento
G = 9.81            # Gravedad
L = 200             # Longitud
MASS = 10           # MASA
TIME_STEP = 0.01   # VELOCIDAD DE MOVIMIENTO

# Initialize pygame
pygame.init()
pygame.display.set_caption("Péndulo Simple")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
#Colores
RED   = (255,0,0)
BLACK = (0,0,0)

# Set up simulation variables
x1 = X1
x2 = X2

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( (255,255,255))

    x1=x1+TIME_STEP*x2
    x2=x2+TIME_STEP*(-(G/L)*math.sin(x1))

    center_x = WIDTH//2
    center_y = HEIGHT//2

    pos_init  = (center_x, center_y)
    pos_final = (center_x+L*math.sin(x1), center_y+L*math.cos(x1))

    pygame.draw.line(screen,RED, pos_init, pos_final, 5 )
    pygame.draw.circle(screen,BLACK, pos_final, 25 )

    
    

    pygame.display.flip()
    
# Quit pygame
pygame.quit()