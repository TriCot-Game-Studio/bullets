import pygame
from bullets.body import Body

BLACK = (0, 0, 0)

body = Body((400, 400), 40, (0, 255, 255))

game_over = False
score = 0
display_size = (500, 500)
fps = 30

pygame.init()


def _quit():
    pygame.display.quit()
    pygame.quit()
    quit()


screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("don't get hit")

# YEP
clock = pygame.time.Clock()

collided = False
while True:
    clock.tick(fps)
    screen.fill(BLACK)
    body.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _quit()

    pygame.display.update()
