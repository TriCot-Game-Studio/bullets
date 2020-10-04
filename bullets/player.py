from .actor import Actor


class Player(Actor):
    def __init__(self, pos, radius, color):
        super().__init__(pos=pos, radius=radius, color=color)
        self.attributes = {"health": 1, "speed": 1}

        self._speed = 10
        self.is_confused = False

        # TODO: should this be in base Body class for other Body objects?
        self.dx = 0
        self.dy = 0

    @property
    def is_alive(self):
        return self.attributes["health"] > 0

    @property
    def speed(self):
        return self._speed * self.attributes["speed"]

    @speed.setter
    def speed(self, x):
        self._speed = x

    @property
    def health(self):
        return self.attributes["health"] * 100

    @health.setter
    def health(self, x):
        self.attributes["health"] += x / 100

    def update(self, w, h):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        if not self.is_offscreen(w, h):
            return

        if self.x < self.radius:
            self.x = self.radius
        elif self.x > w - self.radius:
            self.x = w - self.radius

        if self.y < self.radius:
            self.y = self.radius
        elif self.y > h - self.radius:
            self.y = h - self.radius
