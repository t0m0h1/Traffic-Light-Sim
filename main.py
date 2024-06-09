import pygame


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dim_red = (139, 0, 0)
green = (0, 255, 0)
dim_green = (0, 100, 0) 
yellow = (255, 255, 0)
dim_yellow = (139, 139, 0)

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
    pygame.draw.circle(screen, dim_red, (400, 150), 50)
    pygame.draw.circle(screen, dim_yellow, (400, 300), 50)
    pygame.draw.circle(screen, dim_green, (400, 450), 50)

    pygame.display.update()


screen.mainloop()