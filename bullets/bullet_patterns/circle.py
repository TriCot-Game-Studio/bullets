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

            current_x = self.bullets[i].x
            current_y = self.bullets[i].y
            prev_x = self.x
            prev_y = self.y

            bullet_dx = current_x - prev_x
            bullet_dy = current_y - prev_y

            if not self.bullets[i].is_offscreen(600, 600, fully=False):
                continue
            else:
                for j in range(self.n):
                    self.bullets[j] = Bullet(
                        (self.bullets[i].x, self.bullets[i].y),
                        10,
                        (30, 250, 250),
                        None,
                        bounce=True,
                        dead=False,
                        dx=current_x,
                        dy=current_y,
                    )

    def render(self, screen):
        for bullet in self.bullets:
            if bullet is not None:
                bullet.render(screen)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.update_bullet_locations()
