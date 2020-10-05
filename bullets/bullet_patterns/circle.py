import math
from ..bullet_pattern import BulletPattern
from ..utils import map_range


class CirclePattern(BulletPattern):
    def __init__(self, n, pos, radius, dx=0, dy=0, angle=0):
        super().__init__(n, dx, dy)
        self.x, self.y = pos
        self.radius = radius
        self.angle = angle
        self.update_bullet_locations()

    def update_bullet_locations(self):
        for i in range(self.n):
            if self.bullets[i] is None:
                continue

            angle = map_range(i, 0, self.n, 0, 2 * math.pi)

            angle += self.angle

            x = math.cos(angle) * self.radius
            y = math.sin(angle) * self.radius

            x += self.x
            y += self.y

            self.bullets[i].x = x
            self.bullets[i].y = y

    def render(self, screen):
        for bullet in self.bullets:
            if bullet is not None:
                bullet.render(screen)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.update_bullet_locations()

    # def bounce_or_die(self, screen):
    #     for bullet in self.bullets:
    #         if self.dx < 0 or self.dx > 600 or self.dy < 0 or self.dy > 600:
    #             if not bullet.bounce:
    #                 bullet.render(screen)
    #                 self.update_bullet_locations()
    #             self.dx *= -1
    #             self.dy *= -1
    #         return

    def kill_strays(self, screen):
        strays = []
        for j, bullets in enumerate(self.bullets):
            if bullets is not None:
                self.kill_strays(screen)
                if bullets.dead:
                    strays.append(j)

        for j in strays:
            # noinspection PyTypeChecker
            self.bullets[j] = None
