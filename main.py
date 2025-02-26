import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000,1000))
test_surf = pygame.Surface((100,100))
test_surf.fill('red')
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surf, (500,400))

    
    pygame.display.update()
    clock.tick(60)
