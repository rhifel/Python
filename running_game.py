import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()
running = True

test_surface = pygame.Surface((900,450))
test_surface.fill('red')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(test_surface,(200,150))

    pygame.display.update()
    clock.tick(60)

pygame.quit()