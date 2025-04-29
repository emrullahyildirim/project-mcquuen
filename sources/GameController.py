import pygame
from car import Car  # Car sınıfını içe aktar

class GameController:
    def __init__(self, screen):
        self.screen = screen  # Ekran nesnesini alıyoruz
        self.clock = pygame.time.Clock()
        
        # Araba nesnesini başlat
        self.car = Car(640, 360, 5, (0, 255, 0))  # Araba başlangıç konumu (640, 360), hız 5, yeşil renk

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

    def update(self):
        # Klavye inputlarını işle
        self.car.handle_input()

        # Ekranı temizle
        self.screen.fill((0, 0, 0))  # Ekranı siyah yap

        # Arabayı çiz
        self.car.draw(self.screen)

        pygame.display.flip()  # Ekranı güncelle
