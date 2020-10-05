from .body import Body

DEFAULT_EFFECTS = {"health": -0.1}


class Bullet(Body):
    def __init__(
        self, pos=(0, 0), radius=10, color=(255, 255, 255), effects=None, bounce=False
    ):
        super().__init__(pos=pos, radius=radius, color=color)
        if effects is None:
            effects = DEFAULT_EFFECTS

        self.effects = effects
        self.dead = False
        self.bounce = bounce

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
