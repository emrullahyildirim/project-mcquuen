import pygame
from GameController import GameController
 

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Self Learning Car")

game = GameController(screen)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    game.update()
    clock.tick(60)
