import pygame
from gamecontroller import GameController # type: ignore

pygame.init()

# Ekran boyutunu belirle
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Self Learning Car")

# Oyun kontrolünü başlat
game = GameController(screen)  # GameController sınıfını burada kullanıyoruz

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # Yol resmi
    track = pygame.transform.scale(pygame.image.load("assets/track.png"), (1280, 720))
    screen.blit(track, (0, 0))  # Track görüntüsünü ekrana çiz
    
    # Oyun mantığını güncelle
    game.update()

    pygame.display.flip()
    clock.tick(60)
