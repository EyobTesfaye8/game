import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000,1000))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.Clock()