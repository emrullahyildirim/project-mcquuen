
import pygame

class Car:
    def __init__(self, x=100, y=100):  # varsayılan değer ama değiştirilebilir
        self.image = pygame.Surface((50, 30))  # dikdörtgen gövde
        self.image.fill((255, 0, 0))  # şimşek mcqueen = kırmızı
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # başlangıç konumu
        self.speed = 5

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
