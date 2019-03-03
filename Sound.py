import pygame, sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000)

hit = pygame.mixer.Sound('Bounce.WAV')
hit.play()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
pygame.quit()