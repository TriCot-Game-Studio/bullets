import pygame

from bullets.bullet import Bullet
from bullets.bullet_patterns.circle import CirclePattern
from bullets.player import Player

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_img = pygame.image.load("assets/imgs/gunny.png")

bullet_pattern = CirclePattern(n=18, pos=(300, 300), radius=-50, dx=1, dy=1)
bullet = Bullet(
    pos=(300, 300),
    radius=15,
    color=(255, 100, 50),
    effects=None,
    bounces=True,
    dead=False,
    dx=3,
    dy=2,
)
player = Player(pos=(400, 300), radius=30, color=(255, 255, 0), img=player_img)

game_over = False
score = 0
display_size = (600, 600)
WIDTH, HEIGHT = display_size
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
    screen.fill(GRAY)

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

    if not player.is_alive:
        screen.fill(RED)

    bullet_pattern.angle += 0.05
    bullet_pattern.radius += 1
    bullet_pattern.hit_player(player)
    bullet_pattern.update()
    bullet_pattern.render(screen)

    # bullet.move()
    # bullet.render(screen)

    player.update(WIDTH, HEIGHT)
    player.render(screen)
    pygame.display.update()
