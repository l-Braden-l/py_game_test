import pygame

pygame.init()

widow = pygame.display.set_mode((640,640))

# background = pygame.image.load('indie.jpg').convert()

running = True 
x = 0
while running:

    # widow.blit(background,(x,30))

    x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
    pygame.display.flip()
    pygame.draw.rect(200,200)
    pygame.surface.Surface()
pygame.quit()
