import pygame

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False