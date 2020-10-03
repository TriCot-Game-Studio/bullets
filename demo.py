import pygame
from bullets.bullet_patterns.circle import CirclePattern
from bullets.player import Player

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

bullet_pattern = CirclePattern(20, (400, 400), 200)
player = Player((400, 300), 40, (255, 255, 0))


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _quit()

            # Adjust player velocity on keydown
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                player.dy += 1
            elif event.key in [pygame.K_UP, pygame.K_w]:
                player.dy -= 1
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                player.dx += 1
            elif event.key in [pygame.K_LEFT, pygame.K_a]:
                player.dx -= 1

        elif event.type == pygame.KEYUP:
            # Adjust player velocity on keyup
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                player.dy -= 1
            elif event.key in [pygame.K_UP, pygame.K_w]:
                player.dy += 1
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                player.dx -= 1
            elif event.key in [pygame.K_LEFT, pygame.K_a]:
                player.dx += 1

    if player.is_offscreen(screen.get_width(), screen.get_height()):
        screen.fill(BLUE)

    bullet_pattern.hit_player(player)
    bullet_pattern.render(screen)
    player.update()
    player.render(screen)
    pygame.display.update()
