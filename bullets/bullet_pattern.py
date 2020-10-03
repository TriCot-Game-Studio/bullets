from .bullet import Bullet


class BulletPattern:
    def __init__(self, n):
        self.n = n
        self.bullets = [Bullet() for _ in range(n)]

    def _init_bullet_locations(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def hit_player(self, player):
        for bullet in self.bullets:
            bullet.hit_player(player)
