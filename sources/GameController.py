import pygame
from Car import Car

class GameController:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.car = Car(600, 150, 5, (0, 255, 0))  # Başlangıç konumu

        # Pist görseli ve maskesi
        track_image = pygame.image.load("assets/track.png")
        self.track_image = pygame.transform.scale(track_image, (1280, 720))
        self.track_mask = pygame.mask.from_threshold(self.track_image, (255,255,255), (10,10,10)) #beyaz renk ile siyah rengi ayırma
        
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

    def update(self):
        self.car.handle_input()

        # Pist dışı kontrolü
        car_center_x = int(self.car.x + self.car.width / 2)
        car_center_y = int(self.car.y + self.car.height / 2)

        try:
            if self.track_mask.get_at((car_center_x, car_center_y)) == 0:
                print("Araç pist dışına çıktı!")
                self.car.reset_position()
        except IndexError:
            print("Araç pist dışına çıktı (ekran dışı)!")
            self.car.reset_position()

        # Pist görüntüsünü ekrana çiz
        self.screen.blit(self.track_image, (0, 0))

        # 🔴 Başlangıç çizgisi (kırmızı çizgi)
        pygame.draw.line(self.screen, (255, 0, 0), (665, 50), (665, 260), 5)

        # Araba çizimi
        self.car.draw(self.screen)

        # Ekranı güncelle
        pygame.display.flip()
