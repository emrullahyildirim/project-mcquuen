import pygame

def find_start_position(image_path):
    image = pygame.image.load(image_path)
    width, height = image.get_size()

    for y in range(height):
        for x in range(width):
            r, g, b, *a = image.get_at((x, y))
            if r == 255 and g == 0 and b == 0:  # Saf kırmızı piksel
                return (x, y)
    
    return None  # Hiç kırmızı bulunmazsa
