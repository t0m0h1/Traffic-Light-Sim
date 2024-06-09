import pygame


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Initialize the game
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill(black)
pygame.display.set_caption("Traffic Light Simulation")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(screen, black, (300, 50, 200, 500))
    pygame.draw.circle(screen, red, (400, 150), 50)
    pygame.draw.circle(screen, yellow, (400, 300), 50)
    pygame.draw.circle(screen, green, (400, 450), 50)

    pygame.display.update()


screen.mainloop()