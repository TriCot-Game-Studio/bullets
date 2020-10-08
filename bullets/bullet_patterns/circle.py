import math

from ..bullet import Bullet
from ..bullet_pattern import BulletPattern
from ..utils import map_range


class CirclePattern(BulletPattern):
    def __init__(self, n, pos, radius, dx=0, dy=0, angle=0):
        super().__init__(n, dx, dy)
        self.x, self.y = pos
        self.radius = radius
        self.angle = angle
        self.pattern_broken = False
        self.prev_x = 0
        self.prev_y = 0

        self.update_bullet_locations()

    def update_bullet_locations(self):
        if not self.pattern_broken:
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

                self.bullets[i].dx = self.bullets[i].x - self.prev_x
                self.bullets[i].dy = self.bullets[i].y - self.prev_y

                self.prev_x = self.bullets[i].x
                self.prev_y = self.bullets[i].y

                if self.bullets[i].is_offscreen(600, 600, fully=False):
                    self.pattern_broken = True
        else:
            for i in range(self.n):
                if self.bullets[i] is None:
                    continue
                self.bullets[i].move()

    def render(self, screen):
        for bullet in self.bullets:
            if bullet is not None:
                bullet.render(screen)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.update_bullet_locations()
