import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Self Learning Car")

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit
	track = pygame.transform.scale(pygame.image.load("assets/track.png"), (1280, 720))
	
	screen.blit(track, (0,0))
	
	pygame.display.flip()
	clock.tick(60)