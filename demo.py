import pygame
from bullets.bullet import Bullet
from bullets.player import Player

BLACK = (0, 0, 0)
RED = (255, 0, 0)

bullet = Bullet((400, 400), 31, (0, 255, 255))
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

    # Red if hit
    if not bullet.is_overlapping(player):
        screen.fill(BLACK)
    else:
        screen.fill(RED)

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

    bullet.hit_player(player)
    bullet.render(screen)
    player.update()
    player.render(screen)

    pygame.display.update()
    print(player.health)
