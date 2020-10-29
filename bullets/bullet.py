from .body import Body

DEFAULT_EFFECTS = {"health": -0.1}


class Bullet(Body):
    def __init__(
        self,
        pos=(100, 100),
        radius=20,
        color=(255, 255, 255),
        effects=None,
        bounces=True,
        dead=False,
        dx=0,
        dy=0,
        img=None,
        angle=0,
        is_enemy=False,
        face=False,
    ):
        super().__init__(pos=pos, radius=radius, color=color, img=img, angle=angle)
        if effects is None:
            effects = DEFAULT_EFFECTS

        self.x, self.y = pos
        self.effects = effects
        self.dead = dead

        self.dx = dx
        self.dy = dy
        self.max_speed = 3

        self.bounces = bounces
        self.n_bounces = 0
        self.max_bounces = 2
        self.face = face
        self.is_enemy = is_enemy

    def render(self, screen):
        if not self.dead:
            super().render(screen, self.face)

    def hit_player(self, player):
        if self.is_overlapping(player) and not self.dead:
            self.dead = True

            for key, value in self.effects.items():
                player.attributes[key] += value

    def is_offscreen(self, w, h, fully=True):
        return super().is_offscreen(w, h, fully=fully)

    def update(self):
        if not self.dead:
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
            if self.is_enemy == True:
                if self.dx >= 0:
                    self.face = False
                elif self.dx < 0:
                    self.face = True
            else: 
                self.face = None
                
            # TODO: every 600 in here is really bad,
            #  unless we decide the screen
            #  should *always* be 600 by 600
            self.dead = self.is_offscreen(600, 600)

    def bounce(self):
        if not self.bounces or self.n_bounces >= self.max_bounces:
            return

        if self.x - self.radius < 0 or self.x + self.radius > 600:
            self.dx *= -1
            self.n_bounces += 1
        if self.y - self.radius < 0 or self.y + self.radius > 600:
            self.dy *= -1
            self.n_bounces += 1
