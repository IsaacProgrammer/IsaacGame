import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)


clock = pygame.time.Clock()

x = 0


speed = 250

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    screen.blit(background, (0,0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distancemoved = time_passed_seconds * speed
    x += distancemoved


    if x > 640:
        x -= 540


    pygame.display.update()
