import pygame
from sources.Car import Car
from sources.utils import find_start_position


pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Self Learning Car")

clock = pygame.time.Clock()
# ✅Arabayı oluşturmadan önce haritayı kontrol ediyoruz
start_pos = find_start_position("assets/track2.png")
if start_pos is None:
    print("Haritada kirmizi nokta yok")  # ❌ Başlamadan çıkar
    pygame.quit()
    raise SystemExit


car = Car(*start_pos)  # kırmızı nokta neredeyse oraya başlasın


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit
	
	track = pygame.transform.scale(pygame.image.load("assets/track2.png"), (1280, 720))
	car.handle_keys()
	car_center = car.rect.center  # merkezin koordinatları

	screen.blit(track, (0,0))
	# Arabayla çarpışma kontrolü
	car_center = car.rect.center  # merkezin koordinatları
	pixel_color = track.get_at(car_center)[:3]  # sadece RGB, alpha yok

	if pixel_color != (255,255, 255):  # pist dışıysa
		car.reset_position()

	car.draw(screen)

	
	pygame.display.flip()
	clock.tick(60)