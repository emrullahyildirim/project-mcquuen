import pygame

class Display:
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def tick(self, fps):
        self.clock.tick(fps)

    def quit(self):
        pygame.quit()
