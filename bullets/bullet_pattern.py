from .bullet import Bullet


class BulletPattern:
    def __init__(self, n, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
        self.n = n
        self.bullets = [Bullet() for _ in range(n)]

    def update_bullet_locations(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def hit_player(self, player):
        hit = []
        for i, bullet in enumerate(self.bullets):
            if bullet is not None:
                bullet.hit_player(player)
                if bullet.dead:
                    hit.append(i)

        for i in hit:
            # noinspection PyTypeChecker
            self.bullets[i] = None
