from .body import Body

DEFAULT_EFFECTS = {"health": -0.1}


class Bullet(Body):
    def __init__(
        self,
        pos=(100, 100),
        radius=10,
        color=(255, 255, 255),
        effects=None,
        bounces=True,
        dead=False,
        dx=0,
        dy=0,
    ):
        super().__init__(pos=pos, radius=radius, color=color)
        if effects is None:
            effects = DEFAULT_EFFECTS

        self.x, self.y = pos
        self.effects = effects
        self.dead = dead
        self.bounces = bounces
        self.dx = dx
        self.dy = dy
        self.max_speed = 3

    def render(self, screen):
        if not self.dead:
            super().render(screen)

    def hit_player(self, player):
        if self.is_overlapping(player) and not self.dead:
            self.dead = True

            for key, value in self.effects.items():
                player.attributes[key] += value

    def is_offscreen(self, w, h, fully=True):
        return super().is_offscreen(w, h, fully=fully)

    def move(self):
        self.bounce()
        if self.dx > self.max_speed:
            self.dx = self.max_speed
        elif self.dx < -self.max_speed:
            self.dx = -self.max_speed

        if self.dy > self.max_speed:
            self.dy = self.max_speed
        elif self.dy < -self.max_speed:
            self.dy = -self.max_speed

        self.x += self.dx
        self.y += self.dy

    def bounce(self):
        if (self.x - self.radius < 0 or self.x + self.radius > 600) and self.bounces:
            self.dx *= -1
        if (self.y - self.radius < 0 or self.y + self.radius > 600) and self.bounces:
            self.dy *= -1
