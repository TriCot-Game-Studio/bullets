from bullets import body
from .bullet import Bullet


class BulletPattern:
    def __init__(self, n, dx=0, dy=0, bounce=False):
        self.dx = dx
        self.dy = dy
        self.n = n
        self.bullets = [Bullet() for _ in range(n)]
        self.bounce = bounce

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

        # def bounce_or_die(self, bullet, x, y):
        # if (
        #     self.dx + bullet.radius < 0
        #     or self.dx - bullet.radius > x
        #     or self.dy + bullet.radius < 0
        #     or self.dy - bullet.radius > y
        # ):
        #     if not bullet.bounce:
        #         bullet.dead is True and bullet.render()
        #     self.dx *= -1
        #     self.dy *= -1
