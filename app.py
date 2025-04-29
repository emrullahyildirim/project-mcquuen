import pygame
from sources.Car import Car


pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Self Learning Car")

clock = pygame.time.Clock()
car = Car()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit
	
	track = pygame.transform.scale(pygame.image.load("assets/track.png"), (1280, 720))
	car.handle_keys()
	screen.blit(track, (0,0))
	car.draw(screen)

	
	pygame.display.flip()
	clock.tick(60)