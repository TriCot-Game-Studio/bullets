import math
from ..bullet_pattern import BulletPattern
from ..utils import map_range


class CirclePattern(BulletPattern):
    def __init__(self, n, pos, radius):
        super().__init__(n)
        self.x, self.y = pos
        self.radius = radius

        self._init_bullet_locations()

    def _init_bullet_locations(self):
        for i in range(self.n):
            angle = map_range(i, 0, self.n, 0, 2 * math.pi)
            x = math.cos(angle) * self.radius
            y = math.sin(angle) * self.radius

            x += self.x
            y += self.y

            self.bullets[i].x = x
            self.bullets[i].y = y

    def render(self, screen):
        for bullet in self.bullets:
            bullet.render(screen)

    def update(self):
        pass
