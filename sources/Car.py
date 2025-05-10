import pygame

class Car:
    def __init__(self, x, y, speed, color):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 50
        self.height = 30

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Sol
            self.x -= self.speed
        if keys[pygame.K_d]:  # Sağ
            self.x += self.speed
        if keys[pygame.K_w]:  # Yukarı
            self.y -= self.speed
        if keys[pygame.K_s]:  # Aşağı
            self.y += self.speed

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y
