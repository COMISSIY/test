import pygame, math, random
pygame.init()

sc = pygame.display.set_mode((600, 400))
x, y = 300, 200
a = 0
speed = 2
lenght = 100
trail = [(x, y)]

while True:
	[exit() for i in pygame.event.get() if i.type == pygame.QUIT]
	pygame.time.Clock().tick(60)
	sc.fill((0, 0, 0))
	for i in trail:
		pygame.draw.circle(sc, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (i[0], i[1]), 15)
	x = x + round(speed * math.cos(a))
	y = y + round(speed * math.sin(a))
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		a += 0.1
	if keys[pygame.K_LEFT]:
		a -= 0.1
	if keys[pygame.K_UP]:
		lenght += 1
	if keys[pygame.K_DOWN]:
		lenght -= 1
	trail.append((x, y))
	if lenght < len(trail):
		del trail[0]
	
	pygame.display.update()