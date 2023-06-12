import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()


### Display the image ###

image_surf = pygame.image.load("graphics/bird.png")
image_rect = image_surf.get_rect(center = (0, 300)) # <<< Change me to put the image at different positions
screen.blit(image_surf, image_rect)
n = 1
last = 0
lastx = 0
#########################


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    image_rect.x += max(100/n, 1)
    if image_rect.left > 800:
        image_rect.right = 0
    n += 0.25
    screen.blit(image_surf, image_rect)
    pygame.display.update()
    clock.tick(n)
    print(pygame.time.get_ticks() - last, round((image_rect.x - lastx) % 800 /(pygame.time.get_ticks() - last), 2))
    last = pygame.time.get_ticks()
    lastx = image_rect.x
pygame.quit() 