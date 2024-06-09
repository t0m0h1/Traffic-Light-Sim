import pygame
import sys

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)
LIGHTRED = (255, 100, 100)
LIGHTYELLOW = (255, 255, 100)
LIGHTGREEN = (100, 255, 100)

# Define the initial state and timer
current_light = "RED"
time_counter = 0



current_light = "red"
counter = 0


def draw_traffic_light():
    # Draw the light housing
    pygame.draw.rect(screen, BLACK, (150, 100, 100, 300))
    
    # Draw the red light
    pygame.draw.circle(screen, RED if current_light == "RED" else GRAY, (200, 150), 40)
    
    # Draw the yellow light
    pygame.draw.circle(screen, YELLOW if current_light == "YELLOW" else GRAY, (200, 250), 40)
    
    # Draw the green light
    pygame.draw.circle(screen, GREEN if current_light == "GREEN" else GRAY, (200, 350), 40)


# Initialize the game
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill(BLACK)
pygame.display.set_caption("Traffic Light Simulation")



# Game loop# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the timer and change the light state
    time_counter += 1
    if time_counter == 180:  # Change every 3 seconds (assuming 60 FPS)
        if current_light == "RED":
            current_light = "GREEN"
        elif current_light == "GREEN":
            current_light = "YELLOW"
        elif current_light == "YELLOW":
            current_light = "RED"
        time_counter = 0
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the traffic light
    draw_traffic_light()
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate at 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()
