from .body import Body


class Player(Body):
    def __init__(self, pos, radius, color):
        super().__init__(pos=pos, radius=radius, color=color)
        self.attributes = {"health": 1, "speed": 1}

        self._speed = 2
        self.is_confused = False

        # TODO: should this be in base Body class for other Body objs?
        self.dx = 0
        self.dy = 0

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

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
