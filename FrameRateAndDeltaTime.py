import pygame, sys
from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

test_rect = pygame.Rect(0,310,100,100)
test_speed = 5

while True:
     for event in pygame.event.get():
        if event.type = pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('white')
    
    #rect movement and drawing 
    test_rect.x += test_speed
    pygame.draw.rect(screen,'red',test_rect)
    
    pygame.display.update()
    clock.tick(60)