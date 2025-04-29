import pygame

class Car:
    def __init__(self):
        
        self.rect = pygame.Rect(100, 100, 50, 30)  
        self.color = (255, 0, 0)  
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
        pygame.draw.rect(surface, self.color, self.rect)