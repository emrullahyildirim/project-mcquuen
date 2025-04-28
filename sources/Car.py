import pygame

class Car:
    def __init__(self):
        # Arabamızın başlangıç pozisyonu ve boyutu
        self.rect = pygame.Rect(100, 100, 50, 30)  # (x, y, genişlik, yükseklik)
        self.color = (255, 0, 0)  # Şimşek McQueen kırmızısı
        self.speed = 5  # Arabamızın hareket hızı

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed  # Yukarı hareket
        if keys[pygame.K_s]:
            self.rect.y += self.speed  # Aşağı hareket
        if keys[pygame.K_a]:
            self.rect.x -= self.speed  # Sola hareket
        if keys[pygame.K_d]:
            self.rect.x += self.speed  # Sağa hareket

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
