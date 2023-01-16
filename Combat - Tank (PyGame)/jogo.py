import pygame

from config import WIDTH, HEIGHT, GREEN

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combat - Tank")
clock = pygame.time.Clock()

game_loop = True
while game_loop:

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False